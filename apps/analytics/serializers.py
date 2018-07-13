from rest_framework import serializers

from apps.analytics.models import SMSAnalytics, MisscallAnalytics


class SMSAnalyticsSerializers(serializers.ModelSerializer):
    campaign_name = serializers.ReadOnlyField()

    class Meta:
        model = SMSAnalytics
        fields = '__all__'


class MisscallAnalyticsSerializers(serializers.ModelSerializer):
    campaign_name = serializers.ReadOnlyField()

    class Meta:
        model = MisscallAnalytics
        fields = '__all__'
