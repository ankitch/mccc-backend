from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.utils import perform_search
from .models import Customer, List, Campaign, Segments, SettingConfig, SegmentList
from .serializers import CustomerSerializer, ListSerializer, ListDetailSerializer, CampaignSerializer, \
    CampaignDetailSerializer, SegmentSerializer, SegmentDetailSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('-id')
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class

    @detail_route(methods=['get'])
    def segment(self, request, pk=None, format=None):

        segments = []
        lis = Segments.objects.filter(lists=pk)

        for items in lis:
            segments.append(items.name)

        serializer = SegmentSerializer(lis, many=True).data
        return Response(serializer)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all().order_by('-id')
    serializer_class = CampaignSerializer

    @detail_route(methods=['get'])
    def details(self, request, pk=None, format=None):
        campaign = get_object_or_404(Campaign.objects.prefetch_related('list__customers'), pk=pk)
        serializer = CampaignDetailSerializer(campaign)
        return Response(serializer.data)


class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segments.objects.all().order_by('-id')
    serializer_class = SegmentSerializer
    detail_serializer_class = SegmentDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class


class GetMessage(APIView):
    def get(self, request, format=None, *args, **kwargs):
        campaign_id = kwargs.get('pk')
        segment_id = kwargs.get('segmentpk')

        campaign = get_object_or_404(Campaign, pk=campaign_id)
        get_segment_query = campaign.list.segments.get(pk=segment_id).query

        phone_list = []
        get_template = campaign.template.format(
            url='https://' + request.get_host()
            if request.is_secure()
            else 'http://' + request.get_host() + '/s/' + campaign.short_url.short_code + '/' + str(campaign_id))
        search_result = perform_search(get_segment_query, campaign.list)

        for item in search_result:
            phone_list.append(item.phone)

        return Response({'customers': {'+977': phone_list}, 'template': get_template})


class Settings(APIView):
    def get(self, request, format=None):
        try:
            sets = SettingConfig.get_solo()
            return Response({'attributes': sets.attributes})
        except:
            return Response({'not found'})

    def post(self, request, format=None):
        data = request.data['attributes']
        sets = SettingConfig.get_solo()
        sets.attributes = data
        sets.save()
        return Response({'attributes': sets.attributes})


class AddSegment(APIView):
    def post(self, request, format=None):
        list_id = request.data['list_id']
        segment_id = request.data['segments_id']
        create = SegmentList.objects.create(list_id=list_id, segments_id=segment_id)
        return Response({'segment': "created"})
