from datetime import datetime
from django.core.management import BaseCommand

from apps.send.utils import sync_data_message
from apps.users.models import User


class Command(BaseCommand):
    help = "Syncing request to phone"

    def handle(self, *args, **options):
        user_fcm_reg_ids = User.objects.values('fcm_reg_id')
        print(datetime.now())
        for id in user_fcm_reg_ids:
            if id['fcm_reg_id'] != None:
                print(id['fcm_reg_id'] + "  Sync Request")
                sync_data_message(id['fcm_reg_id'])
        pass
