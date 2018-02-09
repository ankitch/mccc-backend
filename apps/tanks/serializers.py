from django.core.paginator import Paginator

from .models import Customer, List, Campaign
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'full_name','email', 'phone', 'created_at', 'updated_at' )


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
        fields = ('id', 'name', 'customer')


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'list')


class CampaignDetailSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    def get_customers(self, obj):
        lst = []
        for customer in obj.list.coustomers.all():
            try:
                lst.append(customer.phone[0])
            except IndexError:
                pass
        return {'+977': lst}

    class Meta:
        model = Campaign
        fields = ('id', 'name', 'customers')
