from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.send.schedules import schedule_sms
from apps.send.utils import send_sms_fcm
from apps.users.models import User


@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        segment = request.data['segment']
        reg_id = User.objects.get(pk=request.user.id).fcm_reg_id
        send = send_sms_fcm(campaigns, segment, reg_id)
        return send


@api_view(['POST'])
def schedule_campaign(request, *args, **kwargs):
    next_run = request.data.get('next_run')
    sch_type = request.data.get('sch_type')
    repeats = request.data.get('repeat')
    minutes = request.data.get('minutes')
    channel = request.data.get('channels')

    campaigns = request.data.get('campaign')
    segments = request.data.get('segment')

    reg_id = User.objects.get(pk=request.user.id).fcm_reg_id

    sms_func = 'apps.send.api.send_sms_fcm'

    if channel == "SMS":
        sch = schedule_sms(sms_func, campaigns, segments, reg_id, next_run, sch_type, repeats, minutes)

    return Response({'schedule': 'created'})
