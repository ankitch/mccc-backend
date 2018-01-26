import datetime

REST_USE_JWT = True
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=172800),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}
