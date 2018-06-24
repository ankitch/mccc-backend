from drf_haystack.serializers import HaystackSerializer, HaystackSerializerMixin
from drf_haystack.viewsets import HaystackViewSet

from apps.tanks.search_indexes import CustomerIndex


class CustomerSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [CustomerIndex]
        fields = ('full_name', 'text', 'email', 'phone', 'fcm_id', 'lists', 'age', 'sex')


class CustomerSearchView(HaystackViewSet):
    serializer_class = CustomerSearchSerializer
