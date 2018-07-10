import os

from .base import BASE_DIR

# from requests_aws4auth import AWS4Auth

SECRET_KEY = 'nxg=f!y6$z6cti-j5mgjbc#92pb6%(e--9+b)1vvb_-(wyh-dd'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.sendtank.com', 'ec2-18-191-63-240.us-east-2.compute.amazonaws.com']

STATICFILES_DIRS = ()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')

#mero_job_fcm_api_key
FCM_API_KEY_SEND = 'AAAAO00Unqc:APA91bFklxuHBhVD6BeyK0RPGwK3WrdigT-b_xfLlBrf73ZIKLMK82EWuRJ7X48ZmDq1AsWbQMKFUMbmGwzgtEzJGXwNz-HE8A4fnNVfrJg5bqvdoGqtF5P-Pk6IvOVnRxKXqh-WW-08ma'

# awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')

# haystack settings for elastic search
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'https://search-sendtank-xrnnzab7waiyfxguayu476vaie.us-east-2.es.amazonaws.com',
#         'INDEX_NAME': 'sendtank',
#         'KWARGS': {
#             'port': 443,
#             # 'http_auth': awsauth,
#             'use_ssl': True,
#             'verify_certs': True,
#             'connection_class': elasticsearch.RequestsHttpConnection,
#         }
#
#     },
# }

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'https://search-sendtank-zo6jc5r4mxlt7uvbso6meo44e4.us-east-1.es.amazonaws.com'
    },
}
