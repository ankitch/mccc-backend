from django.contrib import admin

# Register your models here.
from apps.url_shortner.models import ShortenedUrl

admin.site.register(ShortenedUrl)
