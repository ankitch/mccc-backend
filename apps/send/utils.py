from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django_q.tasks import async
from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from pyfcm.errors import InvalidDataError
from apps.tanks.models import Campaign
from mccc import settings
from mccc.settings import TEMPLATES


def send_sms_fcm(campaign, segment, fcm_registration_id):
    print(segment)
    if segment == 0:
        data_message = {
            'campaign': campaign,
        }
    else:
        data_message = {
            'campaign': campaign,
            'segment': segment,
        }
    push_service = FCMNotification(
        api_key=settings.FCM_API_KEY_SEND)
    result = None
    try:
        result = push_service.single_device_data_message(
            registration_id=fcm_registration_id,
            data_message=data_message)
    except InvalidDataError:
        raise
    return result


def email_to_ses(query, lists, campaign):
    ses_mail = None
    search_results = perform_search(query, lists)
    campaign = get_object_or_404(Campaign, pk=campaign)
    camp_email = campaign.email_template
    camp_subj = campaign.email_subject
    camp_short = campaign.short_url.short_code
    emails = []
    file_path = campaign.email_template.path
    with open(file_path) as f: email_message = f.read()

    for items in search_results:
        ctx = {
            'user': items.full_name,
            'url': camp_short,
            'email': items.email
        }
        message = EmailMultiAlternatives(subject=camp_subj, body=email_message, from_email=settings.EMAIL_HOST_USER,
                                         to=[items.email])
        email_template = get_template(camp_email).render(ctx)
        message.attach_alternative(email_template, "text/html")
        message.send()
    return ses_mail


def perform_search(query, lists):
    search_query = None
    if 'sex' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=query['sex']))

    elif 'age' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(age=query['age']))

    else:
        search_query = SearchQuerySet().filter(lists=lists)
    return search_query
