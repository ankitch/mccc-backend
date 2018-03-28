from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail

from mccc import settings


def email_to_ses(emails):
    send_mail('Subject here',
              'Sorry this  is a test message',
              'from@example.com',
              emails,
              fail_silently=False, )
    print(emails)


@api_view(['POST', 'GET'])
def send_email(request, *args, **kwargs):
    if request.method == 'POST':
        emails = request.data['emails']
        email_to_ses(emails)
    else:
        print(request.data)

    return Response({'good': 'nice'})


def send_push_notification(title, body, fcm_ids, query, lists):
    perform_search(query, lists)
    push_service = FCMNotification(
        api_key="AAAApd54CKA:APA91bHh60kTOjmJQP8qv8IcQtnkB3-uq-NZtmFGefneT3xlS5dfDEiPUVgjrOKVQdyamgTHn7vIfRvNI6I3vo6nwqW3KntsapmcJIFfJYfrs9a5bYT9VwaRMAVTb6Xzk0Wbm2L5ZEHT")
    # import ipdb
    # ipdb.set_trace()
    result = push_service.notify_multiple_devices(fcm_ids, title, body)
    return Response(result)


@api_view(['POST', 'GET'])
def send_push(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.data['title']
        body = request.data['body']
        fcm_ids = request.data['fcm_ids']
        query = request.data['query']
        lists = request.data['lists']
        # import ipdb
        # ipdb.set_trace()
        return send_push_notification(title, body, fcm_ids, query, lists)


def send_sms_fcm(data):
    data_message = {
        'campaign': data
    }
    push_service = FCMNotification(
        api_key=settings.FCM_API_KEY_SEND)
    result = push_service.single_device_data_message(
        registration_id="dHTO1U7CKP4:APA91bGoXJL6DGySqAInuFv8Eu8KNV8vjpSb1PYX-KZQ3XMCKtWYKCitEOQBE0OUmQ3wt-16HRTy4Cn3leYwKh6ZH7LMLoLWJpEASddNJ9rlzHVYm2cPS3PAsdyXqSEqoisbOe1k5GW3",
        data_message=data_message)

    return Response(result)


@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        return send_sms_fcm(campaigns)

    # import ipdb
    # ipdb.set_trace()
    # send_push_notification(title, body, fcm_ids)


def perform_search(query, lists):
    sexs='male'
    search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=sexs))
    print(query)
    for item in search_query:
        print(item.email)
    # print(search_query)
    import ipdb
    ipdb.set_trace()
