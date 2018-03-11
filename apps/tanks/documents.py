from django_elasticsearch_dsl import DocType, Index, fields
from .models import Customer

customer = Index('customers')

customer.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@customer.doc_type
class CustomerDocument(DocType):
    add_fields = fields.objectfield()

    class Meta:
        model = Customer

        fields = [
            'full_name',
            'email',
            'phone',
        ]

