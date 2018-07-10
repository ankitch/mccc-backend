from rest_framework import serializers

from apps.analytics.models import SMSAnalytics


class SMSAnalyticsSerializers(serializers.ModelSerializer):
    campaign_name = serializers.ReadOnlyField()

    class Meta:
        model = SMSAnalytics
        fields = '__all__'