from django.db.models import Sum
from django_q.models import Task
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.models import ClickEvent, SMSAnalytics, MisscallAnalytics
from apps.analytics.serializers import SMSAnalyticsSerializers, MisscallAnalyticsSerializers
from apps.tanks.models import Customer, Campaign, List
from apps.url_shortner.models import ShortenedUrl


class DashboardAnalytics(APIView):
    def get(self, request, format=None):
        customer_count = Customer.objects.filter(company=request.company).count()
        campaign_count = Campaign.objects.filter(company=request.company).filter(type="Regular").count()
        list_count = List.objects.filter(company=request.company).count()
        total_url_short = ShortenedUrl.objects.count()
        click_event = ClickEvent.objects.aggregate(Sum('count'))
        male_customers = Customer.objects.filter(add_fields__sex="male").filter(company=request.company).count()
        female_customers = Customer.objects.filter(add_fields__sex="female").count()
        failed_task = Task.objects.filter(success=False).count()
        success_task = Task.objects.filter(success=True).count()
        return Response({'customer': customer_count,
                         'campaign': campaign_count,
                         'list': list_count,
                         'gender_data': [['male', male_customers], ['female', female_customers]],
                         'task': [['failed', failed_task], ['success', success_task]],
                         'total_url_short': total_url_short,
                         'total_object_viewed': click_event.get('count__sum')})


class CreateListMixin:
    """Allows bulk creation of a resource."""

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class SMSAnalyticsViewSet(CreateListMixin, viewsets.ModelViewSet):
    queryset = SMSAnalytics.objects.all()
    serializer_class = SMSAnalyticsSerializers


class MisscallAnalyticsViewSet(CreateListMixin, viewsets.ModelViewSet):
    queryset = MisscallAnalytics.objects.all()
    serializer_class = MisscallAnalyticsSerializers


class CampaignAnalytics(generics.ListAPIView):
    serializer_class = SMSAnalyticsSerializers

    def get_queryset(self):
        campaign = self.kwargs['campaign_id']
        return SMSAnalytics.objects.filter(campaign=campaign)


class CampaignMisscallAnalytics(generics.ListAPIView):
    serializer_class = MisscallAnalyticsSerializers

    def get_queryset(self):
        campaign = self.kwargs['campaign_id']
        return MisscallAnalytics.objects.filter(campaign=campaign)