from rest_framework import serializers

from apps.analytics.models import SMSAnalytics


class SMSAnalyticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SMSAnalytics
        fields = '__all__'
