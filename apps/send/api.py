from django.core.mail import send_mail
from django_q.models import Schedule
from django_q.tasks import schedule
from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mccc import settings


def email_to_ses(emails):
    send_mail('Subject here',
              'Sorry this  is a test message',
              'from@example.com ',
              emails,
              fail_silently=False, )
    print(emails)


@api_view(['POST', 'GET'])
def send_email(request, *args, **kwargs):
    if request.method == 'POST':
        emails = []
        query = request.data['query']
        lists = request.data['lists']

        search_results = perform_search(query, lists)

        for items in search_results:
            emails.append(items.email)

        email_to_ses(emails)
    else:
        print(request.data)

    return Response({'good': 'nice'})


def send_push_notification(title, body, query, lists):
    search_results = perform_search(query, lists)
    fcm_ids = []

    for items in search_results:
        fcm_ids.append(items.fcm_id)

    push_service = FCMNotification(
        api_key="AAAApd54CKA:APA91bHh60kTOjmJQP8qv8IcQtnkB3-uq-NZtmFGefneT3xlS5dfDEiPUVgjrOKVQdyamgTHn7vIfRvNI6I3vo6nwqW3KntsapmcJIFfJYfrs9a5bYT9VwaRMAVTb6Xzk0Wbm2L5ZEHT")
    result = push_service.notify_multiple_devices(fcm_ids, title, body)
    return Response(result)


@api_view(['POST', 'GET'])
def send_push(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.data['title']
        body = request.data['body']
        query = request.data['query']
        lists = request.data['lists']
        return send_push_notification(title, body, query, lists)


def send_sms_fcm(campaign, segment):
    data_message = {
        'campaign': campaign,
        'segment': segment,
    }
    print(data_message)
    push_service = FCMNotification(
        api_key=settings.FCM_API_KEY_SEND)
    result = push_service.single_device_data_message(
        registration_id="dHTO1U7CKP4:APA91bGoXJL6DGySqAInuFv8Eu8KNV8vjpSb1PYX-KZQ3XMCKtWYKCitEOQBE0OUmQ3wt-16HRTy4Cn3leYwKh6ZH7LMLoLWJpEASddNJ9rlzHVYm2cPS3PAsdyXqSEqoisbOe1k5GW3",
        data_message=data_message)

    return "{sad}"


@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        segment = request.data['segment']
        return send_sms_fcm(campaigns, segment)


def perform_search(query, lists):
    if 'sex' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=query['sex']))

    elif 'age' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(age=query['age']))

    return search_query


@api_view(['POST'])
def schedule_sms(request, *args, **kwargs):
    campaigns = request.data['campaign']
    segments = request.data['segment']
    nextrun = request.data['next_run'],
    sch_type = request.data['sch_type']
    schedule('apps.send.api.send_sms_fcm', campaign=campaigns, segment=segments,
             hook='apps.send.hooks.print_result', schedule_type=sch_type,
             next_run=nextrun[0], repeats=1)
    return Response({'schedule': 'done'})


def send_command(campaign, segment):
    return send_sms_fcm(campaign, segment)
