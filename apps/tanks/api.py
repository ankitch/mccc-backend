from .serializers import CustomerSerializer, ListSerializer, ListDetailSerializer, CampaignSerializer, \
    CampaignEmailSerializer, SettingsSerializer, CampaignDetailSerializer, SegmentSerializer, SegmentDetailSerializer
from rest_framework import viewsets
from .models import Customer, List, Campaign, Settings, Segments

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('-id')
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

    @detail_route(methods=['get'])
    def details(self, request, pk=None, format=None):
        import ipdb
        ipdb.set_trace()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class


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


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all().order_by('-id')
    serializer_class = SettingsSerializer


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
    print(campaign.emails)
    return Response(campaign.emails)

# @api_view(['POST'])
# def grape_mail_store(request, *args, **kwargs):
#     id = kwargs.get('pk')
#     campaign = Campaign.objects.get(id=id)
#
