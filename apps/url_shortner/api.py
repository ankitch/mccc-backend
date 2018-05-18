from rest_framework import viewsets

from apps.url_shortner.models import ShortenedUrl
from apps.url_shortner.serializers import URLShortSerializer


class ShortenedUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortenedUrl.objects.all().order_by('-id')
    serializer_class = URLShortSerializer
