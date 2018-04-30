from requests import Response
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view

from apps.analytics.models import ObjectViewed
from apps.analytics.serializers import ObjectViewedSerializer


# class ObjectViewSet(viewsets.ModelViewSet):
#     queryset = ObjectViewed.objects.all().order_by('-id')
#     serializer_class = ObjectViewedSerializer

class ObjectViewSet(generics.ListAPIView):
    serializer_class = ObjectViewedSerializer

    def get_queryset(self):
        campaign = self.kwargs['camp_id']
        return ObjectViewed.objects.filter(campaign=campaign)
