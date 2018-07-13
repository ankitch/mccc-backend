from django.contrib import admin

from apps.analytics.models import ClickEvent, SMSAnalytics, MisscallAnalytics

admin.site.register(ClickEvent)
admin.site.register(SMSAnalytics)
admin.site.register(MisscallAnalytics)
