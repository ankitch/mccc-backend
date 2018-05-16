from django.shortcuts import get_object_or_404
from django_q.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.analytics.models import ObjectViewed
from apps.tanks.models import Customer, Campaign, List
from apps.url_shortner.models import ShortenedUrl


@api_view(['GET'])
def dashboard_analytics(request, *args, **kwargs):
    customer = Customer.objects.count()
    campaign = Campaign.objects.count()
    list = List.objects.count()
    total_url_short = ShortenedUrl.objects.count()
    total_object_viewed = ObjectViewed.objects.count()
    male_customers = Customer.objects.filter(add_fields__sex="male").count()
    female_customers = Customer.objects.filter(add_fields__sex="female").count()
    failed_task = Task.objects.filter(success=False).count()
    success_task = Task.objects.filter(success=True).count()

    return Response({'customer': customer,
                     'campaign': campaign,
                     'list': list,
                     'gender_data': [['male', male_customers], ['female', female_customers]],
                     'task': [['failed', failed_task], ['success', success_task]],
                     'total_url_short': total_url_short,
                     'total_object_viewed': total_object_viewed})


@api_view(['GET'])
def chart_data(request, *args, **kwargs):
    campaign = kwargs.get('camp_id')
    male_customers= ObjectViewed.objects.filter(campaign=campaign, customer__add_fields__sex="male").count()
    female_customers= ObjectViewed.objects.filter(campaign=campaign, customer__add_fields__sex="female").count()
    return Response({
        'gender_data': [['male', male_customers], ['female',female_customers]]
    })

