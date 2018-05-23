from django.contrib import admin

from apps.analytics.models import ClickEvent

admin.site.register(ClickEvent)
