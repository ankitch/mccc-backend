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

FCM_API_KEY_SEND = 'AAAA29Kizak:APA91bE8SyRnhLRQNDCyiQyhM5Z0jPyFcrwF_3FRQaYYgT5t3D6CJk9i_svj8qa_3ZgRMlvk0Ll754V4GGFXIJCN7ekiai-yL7-NXW5ICShaIgUdwU2g-OiD9I14aCDXurfv581d0fXCB1pxEvVMG59LrakKvX1jog'

# haystack settings for elastic search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'sendtank',
    },
}
