from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.send.schedules import schedule_sms
from apps.users.models import User
from mccc import settings


def send_sms_fcm(campaign, segment, reg_id):
    data_message = {
        'campaign': campaign,
        'segment': segment,
    }
    push_service = FCMNotification(
        api_key=settings.FCM_API_KEY_SEND)
    result = push_service.single_device_data_message(
        registration_id=reg_id,
        data_message=data_message)
    return result


@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        segment = request.data['segment']
        reg_id = User.objects.get(pk=request.user.id).fcm_reg_id
        send = send_sms_fcm(campaigns, segment, reg_id)
        return send


def perform_search(query, lists):
    search_query = None
    if 'sex' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=query['sex']))

    elif 'age' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(age=query['age']))

    return search_query


@api_view(['POST'])
def schedule_campaign(request, *args, **kwargs):
    name = request.data.get('name')
    next_run = request.data.get('next_run')
    sch_type = request.data.get('sch_type')
    repeats = request.data.get('repeat')
    minutes = request.data.get('minutes')
    channel = request.data.get('channels')

    campaigns = request.data.get('campaign')
    segments = request.data.get('segment')

    query = request.data.get('query')
    lists = request.data.get('lists')
    reg_id = User.objects.get(pk=request.user.id).fcm_reg_id

    sms_func = 'apps.send.api.send_sms_fcm'

    if channel == "SMS":
        sch = schedule_sms(sms_func, campaigns, segments, reg_id, next_run, sch_type, repeats, minutes)

    return Response({'schedule': 'created'})
