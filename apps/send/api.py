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
