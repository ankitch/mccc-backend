from apps.send.utils import sync_data_message
from apps.users.models import User


def push_to_sync():
    user_fcm_reg_ids = User.objects.values('fcm_reg_id')

    for id in user_fcm_reg_ids:
        if id['fcm_reg_id'] != None:
            sync_data_message(id['fcm_reg_id'])
    pass
