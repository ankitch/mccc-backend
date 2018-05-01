from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.analytics.models import ObjectViewed
from apps.tanks.models import Customer, Campaign, List
from apps.url_shortner.models import ShortenedUrl


@api_view(['GET'])
def dashboard_analytics(request, *args, **kwargs):
    # import ipdb
    # ipdb.set_trace()
    customer = Customer.objects.count()
    campaign = Campaign.objects.count()
    list = List.objects.count()
    total_url_short = ShortenedUrl.objects.count()
    total_object_viewed = ObjectViewed.objects.count()

    return Response({'customer': customer,
                     'campaign': campaign,
                     'list': list,
                     'total_url_short': total_url_short,
                     'total_object_viewed': total_object_viewed})
