from django.dispatch import Signal

url_viewed_signal = Signal(providing_args=['cus', 'short', 'request'])
