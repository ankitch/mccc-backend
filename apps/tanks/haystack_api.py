from drf_haystack.serializers import HaystackSerializer, HaystackSerializerMixin
from drf_haystack.viewsets import HaystackViewSet

from apps.tanks.models import Customer
from apps.tanks.search_indexes import CustomerIndex
from apps.tanks.serializers import CustomerSerializer


class CustomerSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [CustomerIndex]
        fields = ('full_name', 'text', 'email', 'phone', 'fcm_id', 'lists', 'age', 'sex')


class CustomerSearchView(HaystackViewSet):
    # index_models = [CustomerIndex]
    serializer_class = CustomerSearchSerializer
