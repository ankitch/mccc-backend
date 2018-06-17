from haystack.query import SearchQuerySet, SQ
from pyfcm import FCMNotification
from pyfcm.errors import InvalidDataError

from mccc import settings


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


def perform_search(query, lists):
    search_query = None
    if 'sex' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(sex=query['sex']))

    elif 'age' in query:
        search_query = SearchQuerySet().filter(SQ(lists=lists) & SQ(age=query['age']))

    else:
        search_query = SearchQuerySet().filter(lists=lists)
    return search_query
