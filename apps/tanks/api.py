from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.utils import perform_search
from .models import Customer, List, Campaign, Segment, SegmentList
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
        queryset = Campaign.objects.filter(company=company).order_by('-id')
        type = self.request.query_params.get('type')
        if type == '"Bulk"':
            queryset = queryset.filter(type="Bulk")

        elif type == '"Regular"':
            queryset = queryset.filter(type="Regular")
        return queryset

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


class AddSegment(APIView):
    def post(self, request, format=None):
        list_id = request.data['list_id']
        segment_id = request.data['segments_id']
        create = SegmentList.objects.create(list_id=list_id, segments_id=segment_id)
        return Response({'segment': "created"})


class CustomerDocumentView(APIView):
    def post(self, request, format=None):
        return ""
# def get(self, request, format=None):
#     from elasticsearch import Elasticsearch
#
#     client = Elasticsearch()
#     list_id = 2
#     key = "add_fields.sex"
#     value = "female"
#     ms = Search(using=client, index="sendtank")
#     ms = ms.from_dict({
#         'query': {
#             'nested': {
#                 'path': 'add_fields',
#                 'query': {
#                     'match': {
#                         key: value
#                     }
#                 }
#             }
#         }
#     })
#     ms = ms.from_dict({
#         'query':{
#             'match':{
#                 'lists':list_id
#             }
#         }
#     })
#     print(ms.to_dict())
#     responses = ms.execute()
#     for response in responses:
#         print(responses)

# ms = MultiSearch(index='sendtank')
#
# ms = ms.add(Search().from_dict({
#     'query': {
#         'nested': {
#             'path': 'add_fields',
#             'query': {
#                 'match': {
#                     key: value
#                 }
#             }
#         }
#     }}))
# ms.filter('match', lists=list_id)
# responses = ms.execute()
# for response in responses:
#     for hit in response:
#         print(hit.full_name)
#
# s = CustomerDocument().search().from_dict({
#     'query': {
#         'nested': {
#             'path': 'add_fields',
#             'query': {
#                 'match': {
#                     key: value
#                 }
#             }
#         }
#     }})
# s = s.from_dict({
#     'query': {
#         'nested': {
#             'path': 'add_fields',
#             'query': {
#                 'match': {
#                     "lists.list_id": list_id
#                 }
#             }
#         }
#     }})

# s = CustomerDocument.search(using=client, index="customer_sendtank") \
# .query("match", lists__list_id=list_id)

# print(response)
# for r in response:
#     print(r.phone + " " + r.email)

# r = s.to_queryset()
#
# import ipdb
# ipdb.set_trace()
#
# # document = CustomerDocument
# serializer_class = CustomerDocumentSerializer
# search_fields = ('full_name', 'email', 'phone', 'lists.lists_id', 'add_fields')
