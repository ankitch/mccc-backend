from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from pyfcm import FCMNotification
from pyfcm.errors import InvalidDataError

from mccc import settings

push_service = FCMNotification(
    api_key=settings.FCM_API_KEY_SEND)


# sends campaign payload to phone
def send_sms_fcm(campaign, segment, fcm_registration_id):
    if segment == 0:
        data_message = {
            'campaign': campaign,
            'type': 'SMS'
        }
    else:
        data_message = {
            'campaign': campaign,
            'segment': segment,
            'type': 'SMS'
        }

    result = None
    try:
        result = push_service.single_device_data_message(
            registration_id=fcm_registration_id,
            data_message=data_message)
    except InvalidDataError:
        raise
    return result


# sends misscall payload to phone
def send_misscall_info(campaign, fcm_reg_id):
    data_message = {
        'campaign': campaign.id,
        'sms_template': campaign.sms_template,
        'type': 'Misscall',
        'status': campaign.misscall_active
    }

    result = None

    try:
        result = push_service.single_device_data_message(
            registration_id=fcm_reg_id,
            data_message=data_message)

    except InvalidDataError:
        raise
    return result


def sync_data_message(fcm_reg_id):
    data_message = {
        'type': 'Sync'
    }
    result = None

    try:
        result = push_service.single_device_data_message(
            registration_id=fcm_reg_id,
            data_message=data_message)

    except InvalidDataError:
        raise
    return result


# performs search and returns response object
def perform_search(query, lists):
    list_id = lists.id
    client = Elasticsearch()
    search_query = Search(using=client, index="sendtank")

    if query:
        key = "add_fields." + list(query.keys())[0]
        value = str(list(query.values())[0])
        search_query = search_query.from_dict({
            'query': {
                'bool': {
                    'filter': [{
                        'match': {
                            'lists': list_id
                        }
                    }],
                    'must': [{
                        'nested': {
                            'path': 'add_fields',
                            'query': {
                                'match': {
                                    key: value
                                }
                            }
                        }
                    }]
                }
            }
        })
    else:
        search_query = search_query.from_dict({
            'query': {
                'match': {
                    'lists': list_id
                }
            }
        })
    # search_query = search_query.filter('match', lists=list_id)
    responses = search_query.execute()
    for response in responses:
        print(response)
    return responses
