from django.core.paginator import Paginator
from rest_framework import serializers

from .models import Customer, List, Campaign, Segment


class CustomerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'email', 'phone', 'lists', 'add_fields', 'created_at', 'updated_at')


class ListSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = List
        fields = ('id', 'name', 'created_at', 'updated_at')


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
        fields = '__all__'


class SegmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = Segment
        fields = ('id', 'name', 'query', 'created_at', 'updated_at')


class SegmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ('id', 'name', 'query')


class CampaignSerializer(serializers.ModelSerializer):
    segments = serializers.SerializerMethodField()
    total_customer = serializers.SerializerMethodField()
    list_name = serializers.SerializerMethodField('get_lists_name')

    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    def get_segments(self, obj):
        page_size = 50
        paginator = Paginator(Segment.objects.filter(lists=obj.list).all(), page_size)
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

    def get_lists_name(self, obj):
        if obj.type == "Bulk":
            return "This is of Bulk Type"

        elif obj.type == "Regular":
            return obj.list.name

        elif obj.type == "Misscall":
            return None

    def get_total_customer(self, obj):
        if obj.type == 'Bulk':
            if (obj.to_numbers is None):
                return "0"
            return str(len(obj.to_numbers))

        elif obj.type == 'Regular':
            return obj.list.customers.count()

    # # validation
    def validate_list(self, data):
        campaign_type = self.initial_data.get('type')

        if campaign_type == 'Bulk':
            raise serializers.ValidationError("This field is not required here.")

        if campaign_type == 'Regular':
            raise serializers.ValidationError("This field is required here.")
        return data

    def validate_to_numbers(self, data):
        campaign_type = self.initial_data.get('type')

        if campaign_type == "Bulk":
            raise serializers.ValidationError("This field is required.")

        elif campaign_type == "Regular":
            return None

        return data

    def validate_name(self, data):
        campaign_type = self.initial_data.get('type')

        if campaign_type == 'Regular':
            raise serializers.ValidationError("This field is required here.")
        return data

    def validate_details(self, data):
        campaign_type = self.initial_data.get('type')

        if campaign_type == 'Regular':
            raise serializers.ValidationError("This field is required here.")
        return data

    class Meta:
        model = Campaign
        fields = ('id', 'name', 'details', 'type', 'to_numbers', 'sms_template', 'list',
                  'total_customer', 'segments', 'list_name', 'misscall_active', 'created_at', 'updated_at',)


class CampaignDetailSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    def get_customers(self, obj):

        lst = []
        if obj.type == "Bulk":
            for customer in obj.to_numbers:
                lst.append(customer)

        elif obj.type == "Regular":
            for customer in obj.list.customers.all():
                lst.append(customer.phone)

        return {'+977': lst}

    class Meta:
        model = Campaign
        fields = ('id', 'name', 'customers', 'sms_template')
