# from .dev import * 
# from .prod import *

SECRET_KEY = '12345'

# postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xxx',
        'USER': 'xx',
        'localhost': 'xxx',
        'PORT': ''
    }
}

FCM_API_KEY_SEND = 'xxx'
