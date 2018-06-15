import os

from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')

AUTH_PASSWORD_VALIDATORS = []

FCM_API_KEY_SEND = 'AAAAO00Unqc:APA91bFklxuHBhVD6BeyK0RPGwK3WrdigT-b_xfLlBrf73ZIKLMK82EWuRJ7X48ZmDq1AsWbQMKFUMbmGwzgtEzJGXwNz-HE8A4fnNVfrJg5bqvdoGqtF5P-Pk6IvOVnRxKXqh-WW-08'
