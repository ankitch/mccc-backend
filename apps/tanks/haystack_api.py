from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from apps.tanks.models import Customer
from apps.tanks.search_indexes import CustomerIndex


class CustomerSerializer(HaystackSerializer):
    class Meta:
        index_classes = [CustomerIndex]
        fields = ['full_name', 'email', 'phone', 'age']


class CustomerSearchView(HaystackViewSet):
    index_models = [Customer]
    serializer_class = CustomerSerializer
