from apps.analytics.models import ObjectViewed
from rest_framework import serializers


class ObjectViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectViewed
        fields = '__all__'
        depth = 3
