from django.shortcuts import get_object_or_404
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.utils import perform_search
from apps.tanks.doc_searializer import CustomerDocumentSerializer
from apps.tanks.documents import CustomerDocument
from .models import Customer, List, Campaign, Segment, SettingConfig, SegmentList
from .serializers import CustomerSerializer, ListSerializer, ListDetailSerializer, CampaignSerializer, \
    CampaignDetailSerializer, SegmentSerializer, SegmentDetailSerializer


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

    def get_queryset(self):
        company = self.request.company
        return List.objects.filter(company=company).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class

    @detail_route(methods=['get'])
    def segment(self, request, pk=None, format=None):
        lis = Segment.objects.filter(lists=pk)
        serializer = SegmentSerializer(lis, many=True).data
        return Response(serializer)


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        company = self.request.company
        return Customer.objects.filter(company=company).order_by('-id')


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        company = self.request.company
        return Campaign.objects.filter(company=company).order_by('-id')

    @detail_route(methods=['get'])
    def details(self, request, pk=None, format=None):
        campaign = get_object_or_404(Campaign.objects.prefetch_related('list__customers'), pk=pk)
        serializer = CampaignDetailSerializer(campaign)
        return Response(serializer.data)


class SegmentViewSet(viewsets.ModelViewSet):
    serializer_class = SegmentSerializer
    detail_serializer_class = SegmentDetailSerializer

    def get_queryset(self):
        company = self.request.company
        return Segment.objects.filter(company=company).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class


class GetMessage(APIView):
    def get(self, request, format=None, *args, **kwargs):
        campaign_id = kwargs.get('pk')
        segment_id = kwargs.get('segmentpk')

        campaign = get_object_or_404(Campaign, pk=campaign_id)
        get_segment_query = {}

        if segment_id != 0:
            get_segment_query = campaign.list.segments.get(pk=segment_id).query

        phone_list = []
        get_template = campaign.sms_template.format(
            url='https://' + request.get_host()
            if request.is_secure() else 'http://' + request.get_host() + '/s/' + campaign.short_url.short_code + '/' + str(
                campaign_id))

        search_result = perform_search(get_segment_query, campaign.list)

        for item in search_result:
            phone_list.append(item.phone)

        return Response({'customers': {'+977': phone_list}, 'sms_template': get_template})


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


class CustomerDocumentView(BaseDocumentViewSet):
    document = CustomerDocument
    serializer_class = CustomerDocumentSerializer
    search_fields = ('full_name', 'email', 'phone', 'lists', 'add_fields')
