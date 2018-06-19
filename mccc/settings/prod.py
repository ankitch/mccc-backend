import os
from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, TEMPLATES
SECRET_KEY = 'nxg=f!y6$z6cti-j5mgjbc#92pb6%(e--9+b)1vvb_-(wyh-dd'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.sendtank.com', 'ec2-18-191-63-240.us-east-2.compute.amazonaws.com']

STATICFILES_DIRS = ()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')

FCM_API_KEY_SEND = "AAAAQvw3CNQ:APA91bHEdh46Gd7q6yJ2L4pjowxLE0Alg5MWQ32id3iV51AEaf5D1HLDGsABTR3Z1mfbFP5g8aQ02EJ1D1Yif2prvabMhndtshZQ03jEDxQQEeuIIJoTeRRrLXrRrLJn5zdrMhnZHp-9"
