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

