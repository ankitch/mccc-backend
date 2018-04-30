from apps.analytics.models import ObjectViewed
from rest_framework import serializers


class ObjectViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectViewed
        fields = ('id', 'timestamp', 'customer', 'campaign')
        depth = 3
