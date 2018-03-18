from pyfcm import FCMNotification
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail


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


def send_push_notification(title, body, fcm_ids):
    push_service = FCMNotification(api_key= "AAAApd54CKA:APA91bHh60kTOjmJQP8qv8IcQtnkB3-uq-NZtmFGefneT3xlS5dfDEiPUVgjrOKVQdyamgTHn7vIfRvNI6I3vo6nwqW3KntsapmcJIFfJYfrs9a5bYT9VwaRMAVTb6Xzk0Wbm2L5ZEHT")
    result = push_service.notify_multiple_devices(fcm_ids,title,body)
    print(result)


@api_view(['POST', 'GET'])
def send_push(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.data['title']
        body = request.data['body']
        fcm_ids = request.data['fcm_ids']

        send_push_notification(title, body, fcm_ids)

    else:
        print(request.data)
    return Response({'good': 'push'})