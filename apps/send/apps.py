from django.apps import AppConfig


class SendConfig(AppConfig):
    name = 'send'

    def ready(self):
        print("App config run")
        import ipdb
        ipdb.set_trace( )
        # from datetime import datetime
        #
        # _date = datetime.now()
        # date = datetime(_date.year, _date.month, _date.day)

