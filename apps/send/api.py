  from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.schedules import schedule_sms
from apps.send.utils import send_sms_fcm
from apps.users.models import User


class SendSMS(APIView):
    def post(self, request, format=None):
        campaign = request.data['campaign']
        segment = request.data['segment']
        reg_id = User.objects.get(pk=request.user.id).fcm_reg_id
        send = send_sms_fcm(campaign, segment, reg_id)
        return Response(send)


class ScheduleCampaign(APIView):
    def post(self, request, format=None):
        next_run = request.data.get('next_run')
        schedule_type = request.data.get('sch_type')
        repeats = request.data.get('repeat')
        minutes = request.data.get('minutes')
        channel = request.data.get('channels')

        campaigns = request.data.get('campaign')
        segments = request.data.get('segment')

        fcm_registration_id = User.objects.get(pk=request.user.id).fcm_reg_id

        sms_func = 'apps.send.utils.py.send_sms_fcm'

        if channel == "SMS":
            sch = schedule_sms(sms_func, campaigns, segments, fcm_registration_id, next_run, schedule_type, repeats, minutes)

        return Response({'schedule': 'created'})