from django_q.models import Task
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.models import ClickEvent
from apps.tanks.models import Customer, Campaign, List
from apps.url_shortner.models import ShortenedUrl


class DashboardAnalytics(APIView):
    def get(self, request, format=None):
        customer_count = Customer.objects.count()
        campaign_count = Campaign.objects.count()
        list_count = List.objects.count()
        total_url_short = ShortenedUrl.objects.count()

        total_count = 0
        click_event = ClickEvent.objects.all()
        for item in click_event:
            total_count += item.count
        male_customers = Customer.objects.filter(add_fields__sex="male").count()
        female_customers = Customer.objects.filter(add_fields__sex="female").count()
        failed_task = Task.objects.filter(success=False).count()
        success_task = Task.objects.filter(success=True).count()

        return Response({'customer': customer_count,
                         'campaign': campaign_count,
                         'list': list_count,
                         'gender_data': [['male', male_customers], ['female', female_customers]],
                         'task': [['failed', failed_task], ['success', success_task]],
                         'total_url_short': total_url_short,
                         'total_object_viewed': total_count})
