from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from apps.tanks.documents import CustomerDocument


class CustomerDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CustomerDocument
        fields =('full_name', 'email', 'phone', 'lists', 'add_fields')