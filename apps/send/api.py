from django.core.mail import send_mail
from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.send.schedules import schedule_sms, schedule_email_push, trigger_all
from apps.tanks.models import Campaign
from mccc import settings


def email_to_ses(query, lists, campaign):
    mail = None
    search_results = perform_search(query, lists)
    email_template = Campaign.objects.get(pk=campaign).emails
    email_subject = Campaign.objects.get(pk=campaign).email_subject
    short_code = Campaign.objects.get(pk=campaign).short_url.short_code

    for items in search_results:
        send = email_template.format(url='http://127.0.0.1:8000/s1/' + short_code  + '/' + items.pk + "/" + str(campaign))
        ses_mail = send_mail(email_subject,
                             send,
                             'from@example.com',
                             [items.email],
                             fail_silently=False, )
    return mail


@api_view(['POST', 'GET'])
def email_view(request, *args, **kwargs):
    if request.method == 'POST':
        query = request.data['query']
        lists = request.data['lists']
        campaign_id = request.data['campaign_id']
        return send_email(query, lists, campaign_id)

    else:
        print(request.data)


def send_email(query, lists, campaign_id):
    email = email_to_ses(query, lists, campaign_id)
    return Response(email)


def send_push_notification(query, lists, campaign):
    title_push = Campaign.objects.get(pk=campaign).push_title
    body_push = Campaign.objects.get(pk=campaign).push_body
    search_results = perform_search(query, lists)
    fcm_ids = []
    for items in search_results:
        fcm_ids.append(items.fcm_id)

    push_service = FCMNotification(
        api_key="AAAApd54CKA:APA91bHh60kTOjmJQP8qv8IcQtnkB3-uq-NZtmFGefneT3xlS5dfDEiPUVgjrOKVQdyamgTHn7vIfRvNI6I3vo6nwqW3KntsapmcJIFfJYfrs9a5bYT9VwaRMAVTb6Xzk0Wbm2L5ZEHT")
    result = push_service.notify_multiple_devices(fcm_ids,  body_push, title_push,)
    return result


@api_view(['POST', 'GET'])
def send_push(request, *args, **kwargs):
    if request.method == 'POST':
        query = request.data['query']
        lists = request.data['lists']
        campaign = request.data['campaign']
        send_push = send_push_notification(query, lists, campaign)
        return Response(send_push)


def send_sms_fcm(campaign, segment):
    data_message = {
        'campaign': campaign,
        'segment': segment,
    }
    push_service = FCMNotification(
        api_key=settings.FCM_API_KEY_SEND)

    result = push_service.single_device_data_message(
        registration_id="eBFECJ5vSvU:APA91bHYp4xgJt3ea8gSmCjpnhj4OuBmChtDSz8GK38o3xkuTcUWOgTeyUE7amJhv8LrCNoRQLZixIBlcoMs_eJg3Y0W9fVuI6gCnLvDENPWZ_vIfaYrE4QNjPjQeS9TnnlLepCLRt13",
        data_message=data_message)
    print(result)
    print(campaign, segment)
    return result


@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        segment = request.data['segment']
        send = send_sms_fcm(campaigns, segment)
        return Response(send)


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

    sms_func = 'apps.send.api.send_sms_fcm'
    email_func = 'apps.send.api.email_to_ses'
    push_func = 'apps.send.api.send_push_notification'

    if channel == "SMS":
        sch = schedule_sms(sms_func, campaigns, segments, next_run, sch_type, repeats, minutes)
    elif channel == "Email":
        sch = schedule_email_push(email_func, query, lists, campaigns, next_run, sch_type, repeats, minutes)

    elif channel == "Push":
        sch = schedule_email_push(push_func, query, lists, campaigns, next_run, sch_type, repeats, minutes)

    elif channel == "All":
        sch = trigger_all(push_func, email_func, sms_func, campaigns, segments, query, lists, next_run, sch_type,
                          repeats, minutes)

    return Response({'schedule': 'created'})
