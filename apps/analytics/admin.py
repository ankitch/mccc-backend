from django.contrib import admin

from apps.analytics.models import ClickEvent, SMSAnalytics

admin.site.register(ClickEvent)
admin.site.register(SMSAnalytics)
