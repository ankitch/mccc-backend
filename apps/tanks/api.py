from .serializers import CustomerSerializer, ListSerializer, ListDetailSerializer, CampaignSerializer, \
    CampaignEmailSerializer, SettingsSerializer
from rest_framework import viewsets
from .models import Customer, List, Campaign, Settings

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('-id')
    serializer_class = ListSerializer
    detail_serializer_class = ListDetailSerializer

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


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all().order_by('-id')
    serializer_class = SettingsSerializer


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
