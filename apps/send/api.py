from django.core.mail import send_mail
from django_q.tasks import schedule
from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mccc import settings


def email_to_ses(emails):
    send_mail('Subject here',
              'Sorry this  is a test message',
              'from@example.com',
              emails,
              fail_silently=False, )
    print(emails)
    return Response({'Status': 'email delivered'})


@api_view(['POST', 'GET'])
def email_view(request, *args, **kwargs):
    if request.method == 'POST':
        query = request.data['query']
        lists = request.data['lists']
        return send_email(query, lists)

    else:
        print(request.data)


def send_email(query, lists):
    search_results = perform_search(query, lists)
    emails = []
    for items in search_results:
        emails.append(items.email)

    return email_to_ses(emails)


# TODO
# to enable push notification by getting body
def send_push_notification(query, lists):
    search_results = perform_search(query, lists)
    fcm_ids = []
    title = "title"
    body = "body"
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
        return send_push_notification(query, lists)


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


# @api_view(['POST'])
# def schedule_sms(request, *args, **kwargs):
#     name = request.data.get('name')
#     campaigns = request.data.get('campaign')
#     segments = request.data.get('segment')
#     next_run = request.data.get('next_run')
#     sch_type = request.data.get('sch_type')
#     repeats = request.data.get('repeat')
#     minutes = request.data.get('minutes')
#
#     if sch_type == 'O':
#         schedule('apps.send.api.send_sms_fcm', campaign=campaigns, segment=segments,
#                  name=name,
#                  hook='apps.send.hooks.print_result', schedule_type=sch_type,
#                  next_run=next_run)
#
#     elif sch_type == 'I':
#         schedule('apps.send.api.send_sms_fcm', campaign=campaigns, segment=segments,
#                  name=name,
#                  hook='apps.send.hooks.print_result', schedule_type=sch_type,
#                  next_run=next_run, repeats=repeats, minutes=minutes)
#
#     else:
#         schedule('apps.send.api.send_sms_fcm', campaign=campaigns, segment=segments,
#                  name=name,
#                  hook='apps.send.hooks.print_result', schedule_type=sch_type,
#                  next_run=next_run, repeats=repeats)
#
#     return Response({'schedule': 'done'})


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
    email_func = 'apps.send.api.send_email'
    push_func = 'apps.send.api.send_push_notification'

    if channel == "SMS":
        schedule_sms(sms_func, name, campaigns, segments, next_run, sch_type, repeats, minutes)
    elif channel == "Email":
        schedule_email_push(email_func, name, query, lists, next_run, sch_type, repeats, minutes)

    elif channel == "Push":
        schedule_email_push(push_func, name, query, lists, next_run, sch_type, repeats, minutes)

    # Todo
    # trigger all
    elif channel == "All":
        trigger_all(push_func, email_func, campaigns, segments, sms_func, name, query, lists, next_run, sch_type, repeats, minutes)

    return Response({'schedule': 'done'})


def schedule_sms(trigger_func, name, campaign, segment, next_run, sch_type, repeats, minutes):
    if sch_type == 'O':
        schedule(trigger_func,
                 campaign=campaign,
                 segment=segment,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run)

    elif sch_type == 'I':
        schedule(trigger_func,
                 campaign=campaign,
                 segment=segment,
                 name=name,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        schedule(trigger_func,
                 campaign=campaign,
                 segment=segment,
                 name=name,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run, repeats=repeats)


def schedule_email_push(trigger_func, name, query, lists, next_run, sch_type, repeats, minutes):
    if sch_type == 'O':
        schedule(trigger_func,
                 query=query,
                 lists=lists,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run)

    elif sch_type == 'I':
        schedule(trigger_func,
                 query=query,
                 lists=lists,
                 name=name,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        schedule(trigger_func,
                 query=query,
                 lists=lists,
                 name=name,
                 hook='apps.send.hooks.print_result', schedule_type=sch_type,
                 next_run=next_run, repeats=repeats)


def trigger_all(push_func, email_func, campaign, segment, sms_func, name, query, lists, next_run, sch_type, repeats, minutes):
    schedule_sms(sms_func, name, campaign, segment, next_run, sch_type, repeats, minutes)
    schedule_email_push(email_func, name, query, lists, next_run, sch_type, repeats, minutes)
    schedule_email_push(push_func, name, query, lists, next_run, sch_type, repeats, minutes)
