from django_elasticsearch_dsl import DocType, Index, fields

from apps.tanks.models import Customer

customer = Index('sendtank')
customer.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@customer.doc_type
class CustomerDocument(DocType):
    id = fields.IntegerField()
    full_name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    lists = fields.ListField(field=fields.IntegerField())
    add_fields = fields.NestedField()

    def prepare_add_fields(self, instance):
        return instance.add_fields

    def prepare_lists(self, instance):
        return [list.id for list in instance.lists.all()]

    class Meta:
        model = Customer
        queryset_pagination = 1000
