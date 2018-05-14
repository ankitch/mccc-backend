import os 
from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, TEMPLATES 
SECRET_KEY = 'nxg=f!y6$z6cti-j5mgjbc#92pb6%(e--9+b)1vvb_-(wyh-dd'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.sendtank.com']

STATICFILES_DIRS = ()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')

