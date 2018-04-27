from django.contrib import admin

# Register your models here.
from apps.analytics.models import ObjectViewed
from apps.url_shortner.models import ShortenedUrl

admin.site.register(ShortenedUrl)
admin.site.register(ObjectViewed)
