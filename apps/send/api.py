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
    push_service = FCMNotification(
        api_key="AAAApd54CKA:APA91bHh60kTOjmJQP8qv8IcQtnkB3-uq-NZtmFGefneT3xlS5dfDEiPUVgjrOKVQdyamgTHn7vIfRvNI6I3vo6nwqW3KntsapmcJIFfJYfrs9a5bYT9VwaRMAVTb6Xzk0Wbm2L5ZEHT")
    # import ipdb
    # ipdb.set_trace()
    result = push_service.notify_multiple_devices(fcm_ids, title, body)
    print(result)


@api_view(['POST', 'GET'])
def send_push(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.data['title']
        body = request.data['body']
        fcm_ids = request.data['fcm_ids']
        # import ipdb
        # ipdb.set_trace()
        send_push_notification(title, body, fcm_ids)

    else:
        print(request.data)
    return Response({'good': 'push'})


def send_sms_fcm(data):
    data_message = {
        'campaign':data
    }
    push_service = FCMNotification(api_key="AAAAQvw3CNQ:APA91bHEdh46Gd7q6yJ2L4pjowxLE0Alg5MWQ32id3iV51AEaf5D1HLDGsABTR3Z1mfbFP5g8aQ02EJ1D1Yif2prvabMhndtshZQ03jEDxQQEeuIIJoTeRRrLXrRrLJn5zdrMhnZHp-9")
    result = push_service.single_device_data_message(registration_id="dHTO1U7CKP4:APA91bGoXJL6DGySqAInuFv8Eu8KNV8vjpSb1PYX-KZQ3XMCKtWYKCitEOQBE0OUmQ3wt-16HRTy4Cn3leYwKh6ZH7LMLoLWJpEASddNJ9rlzHVYm2cPS3PAsdyXqSEqoisbOe1k5GW3",
                                                     data_message=data_message)

    print(result)

@api_view(['POST', 'GET'])
def send_sms(request, *args, **kwargs):
    if request.method == 'POST':
        campaigns = request.data['campaign']
        send_sms_fcm(campaigns)

    return Response({'good', 'sms'})
    # import ipdb
    # ipdb.set_trace()
    # send_push_notification(title, body, fcm_ids)
