from django.core.paginator import Paginator
from rest_framework import serializers

from .models import Customer, List, Campaign, Segments, SettingConfig


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'email', 'phone', 'lists', 'add_fields', 'created_at', 'updated_at')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingConfig
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


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segments
        fields = ('id', 'name', 'query', 'created_at', 'updated_at')


class SegmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segments
        fields = ('id', 'name', 'query')


class CampaignSerializer(serializers.ModelSerializer):
    segments = serializers.SerializerMethodField()

    def get_segments(self, obj):
        page_size = 50
        paginator = Paginator(Segments.objects.filter(lists=obj.list).all(), page_size)
        object_list = paginator.page(1)
        serializer = SegmentSerializer(object_list, many=True)
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

    list_name = serializers.SerializerMethodField('get_lists_name')

    class Meta:
        model = Campaign
        fields = (
            'id', 'name', 'details', 'list', 'short_url', 'created_at', 'updated_at', 'segments', 'template',
            'list_name')

    def get_lists_name(self, obj):
        return obj.list.name


class CampaignDetailSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    def get_customers(self, obj):
        lst = []
        for customer in obj.list.customers.all():
            lst.append(customer.phone)

        return {'+977': lst}

    class Meta:
        model = Campaign
        fields = ('id', 'name', 'customers', 'template')
