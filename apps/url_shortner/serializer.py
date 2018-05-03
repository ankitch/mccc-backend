from rest_framework import serializers

from apps.url_shortner.models import ShortenedUrl


class URLShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = '__all__'
