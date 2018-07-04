from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from apps.tanks.documents import CustomerDocument


class CustomerDocumentSerializer(DocumentSerializer):
    # id = serializers.IntegerField(read_only=True)
    # full_name = serializers.CharField(read_only=True)
    # email = serializers.CharField(read_only=True)
    # phone = serializers.CharField(read_only=True)
    # lists = serializers.SerializerMethodField()
    # add_fields = serializers.JSONField(read_only=True)

    class Meta(object):
        document = CustomerDocument
        fields = ('id', 'full_name', 'email', 'phone', 'lists', 'add_fields')
