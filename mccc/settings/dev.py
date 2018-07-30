from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.122']
INTERNAL_IPS = ['127.0.0.1']

STATICFILES_DIRS = ()

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTH_PASSWORD_VALIDATORS = []

FCM_API_KEY_SEND = 'AAAAO00Unqc:APA91bFklxuHBhVD6BeyK0RPGwK3WrdigT-b_xfLlBrf73ZIKLMK82EWuRJ7X48ZmDq1AsWbQMKFUMbmGwzgtEzJGXwNz-HE8A4fnNVfrJg5bqvdoGqtF5P-Pk6IvOVnRxKXqh-WW-08'

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
ELASTICSEARCH_DSL_AUTO_REFRESH = True
ELASTICSEARCH_DSL_SIGNAL_PROCESSOR = 'django_elasticsearch_dsl.signals.RealTimeSignalProcessor'
