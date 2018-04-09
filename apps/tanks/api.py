from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response

from apps.send.api import perform_search
from .models import Customer, List, Campaign, Segments, SettingConfig, SegmentList
from .serializers import CustomerSerializer, ListSerializer, ListDetailSerializer, CampaignSerializer, CampaignDetailSerializer, SegmentSerializer, SegmentDetailSerializer


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
            try:
                segments.append(items.name)
            except IndexError:
                pass

        serializer = SegmentSerializer(lis, many=True).data
        return Response(serializer)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all().order_by('-id')
    serializer_class = CampaignSerializer

    # todo change to post
    @detail_route(methods=['get'])
    def trigger(self, request, pk=None, format=None):
        campaign = get_object_or_404(Campaign, pk=pk)
        campaign.trigger()
        return Response({})

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


@api_view(['GET'])
def grape_mail_load(request, *args, **kwargs):
    id = kwargs.get('pk')
    campaign = Campaign.objects.get(id=id)

    return Response(campaign.emails)


@api_view(['GET'])
def segment(request, *args, **kwargs):
    campaign_id = kwargs.get('pk')
    segment_id = kwargs.get('segmentpk')

    get_template = Campaign.objects.get(pk=campaign_id).template
    get_segment = Campaign.objects.get(pk=campaign_id).list.segments.get(pk=segment_id).query
    get_lists = Campaign.objects.get(pk=campaign_id).list
    phone_list = []

    search_result = perform_search(get_segment, get_lists)
    for item in search_result:
        phone_list.append(item.phone)

    return Response({'customers': {'+977': phone_list}, 'template': get_template})


# for settings singleton
# class
# config = SettingConfig.get_solo()


@api_view(['GET', 'POST'])
def create_settings(request, *args, **kwargs):
    if request.method == 'GET':
        sets = SettingConfig.objects.get(pk=1)
        return Response({'attributes': sets.attributes})

    elif request.method == 'POST':
        data = request.data['attributes']
        sets = SettingConfig.objects.get(pk=1)
        sets.attributes = data
        sets.save()
        return Response({'attributes': sets.attributes})


@api_view(['POST'])
def create_list_segment(request, *args, **kwargs):
    list_id = request.data['list_id']
    segment_id = request.data['segments_id']
    print(list_id, segment_id)
    create = SegmentList.objects.create(list_id=list_id, segments_id=segment_id)
    print(create)
    return Response({'create': "sads"})
