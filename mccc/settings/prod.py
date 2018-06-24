import elasticsearch
import os
# from requests_aws4auth import AWS4Auth

from .base import BASE_DIR

SECRET_KEY = 'nxg=f!y6$z6cti-j5mgjbc#92pb6%(e--9+b)1vvb_-(wyh-dd'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.sendtank.com', 'ec2-18-191-63-240.us-east-2.compute.amazonaws.com']

STATICFILES_DIRS = ()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')

FCM_API_KEY_SEND = "AAAAQvw3CNQ:APA91bHEdh46Gd7q6yJ2L4pjowxLE0Alg5MWQ32id3iV51AEaf5D1HLDGsABTR3Z1mfbFP5g8aQ02EJ1D1Yif2prvabMhndtshZQ03jEDxQQEeuIIJoTeRRrLXrRrLJn5zdrMhnZHp-9"

# awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')

# haystack settings for elastic search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'https://search-sendtank-xrnnzab7waiyfxguayu476vaie.us-east-2.es.amazonaws.com',
        'INDEX_NAME': 'sendtank',
        'KWARGS': {
            'port': 443,
            # 'http_auth': awsauth,
            'use_ssl': True,
            'verify_certs': True,
            'connection_class': elasticsearch.RequestsHttpConnection,
        }

    },
}
