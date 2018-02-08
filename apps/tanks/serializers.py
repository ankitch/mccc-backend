from django.core.paginator import Paginator

from .models import Customer, List
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class ListDetailSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()

    def get_customer(self, obj):
        page_size = 50
        paginator = Paginator(obj.customers.all(), page_size)
        object_list = paginator.page(1)
        serializer = CustomerSerializer(object_list, many=True)
        count = object_list.paginator.count
        if page_size > count:
            page_size = count
        return {
            'count': count,
            'page_size': page_size,
            'page': object_list.number,
            'pages': object_list.paginator.num_pages,
            'results': serializer.data,
        }

    class Meta:
        model = List
        fields = ('id','name', 'customer')
