from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INTERNAL_IPS = ['127.0.0.1']

STATICFILES_DIRS = ()

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTH_PASSWORD_VALIDATORS = []

FCM_API_KEY_SEND = "AAAAQvw3CNQ:APA91bHEdh46Gd7q6yJ2L4pjowxLE0Alg5MWQ32id3iV51AEaf5D1HLDGsABTR3Z1mfbFP5g8aQ02EJ1D1Yif2prvabMhndtshZQ03jEDxQQEeuIIJoTeRRrLXrRrLJn5zdrMhnZHp-9"
