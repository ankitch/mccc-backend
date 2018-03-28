import os

from .base import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nxg=f!y6$z6cti-j5mgjbc#92pb6%(e--9+b)1vvb_-(wyh-dd'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.122', '192.168.0.103']
INTERNAL_IPS = ['127.0.0.1']

STATICFILES_DIRS = ()

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mccc',
        'USER': 'ankit',
        'localhost': 'localhost',
        'PORT': ''
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#
FCM_API_KEY_SEND="AAAAQvw3CNQ:APA91bHEdh46Gd7q6yJ2L4pjowxLE0Alg5MWQ32id3iV51AEaf5D1HLDGsABTR3Z1mfbFP5g8aQ02EJ1D1Yif2prvabMhndtshZQ03jEDxQQEeuIIJoTeRRrLXrRrLJn5zdrMhnZHp-9"

