from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification

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


def perform_search(query, lists):
    search_query = None
    if 'sex' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=query['sex']))

    elif 'age' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(age=query['age']))

    return search_query
