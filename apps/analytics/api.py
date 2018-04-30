from rest_framework import viewsets

from apps.analytics.models import ObjectViewed
from apps.analytics.serializers import ObjectViewedSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = ObjectViewed.objects.all().order_by('-id')
    serializer_class = ObjectViewedSerializer
