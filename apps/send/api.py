from django_q.tasks import async
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.schedules import schedule_sms, schedule_email_push, trigger_all
from apps.send.utils import send_sms_fcm, email_to_ses
from apps.users.models import User


class SendSMS(APIView):
    def post(self, request, format=None):
        campaign = request.data['campaign']
        segment = request.data['segment']
        reg_id = User.objects.get(pk=request.user.id).fcm_reg_id
        send = send_sms_fcm(campaign, segment, reg_id)
        return Response(send)


class SendEmail(APIView):
    def post(self, request, format=None):
        query = request.data['query']
        lists = request.data['lists']
        campaign_id = request.data['campaign_id']
        if query == None:
            query = {}
        return send_email(query, lists, campaign_id)


def send_email(query, lists, campaign_id):
    email = async(email_to_ses(query, lists, campaign_id))
    return Response(email)


class ScheduleCampaign(APIView):
    def post(self, request, format=None):
        next_run = request.data.get('next_run')
        schedule_type = request.data.get('sch_type')
        repeats = request.data.get('repeat')
        minutes = request.data.get('minutes')
        channel = request.data.get('channels')

        campaigns = request.data.get('campaign')
        segments = request.data.get('segment')
        query = request.data.get('query')
        print(minutes)
        if query == None:
            query = {}
        lists = request.data.get('lists')
        fcm_registration_id = User.objects.get(pk=request.user.id).fcm_reg_id

        sms_func = 'apps.send.utils.py.send_sms_fcm'
        email_func = 'apps.send.utils.email_to_ses'

        if channel == "SMS":
            sch = schedule_sms(sms_func, campaigns, segments, fcm_registration_id, next_run, schedule_type, repeats, minutes)
        elif channel == "Email":
            sch = schedule_email_push(
                email_func, query, lists, campaigns, next_run, schedule_type, repeats,
                minutes)
        elif channel == "All":
            sch = trigger_all(email_func, sms_func, campaigns, segments,
                              query, lists, next_run, schedule_type,
                              repeats, minutes)
        return Response({'schedule': 'created'})
