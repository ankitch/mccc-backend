from django.contrib import admin

# Register your models here.
from apps.analytics.models import ClickEvent

admin.site.register(ClickEvent)
