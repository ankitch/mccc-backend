from django_elasticsearch_dsl import DocType, Index, fields

from apps.tanks.models import Customer

customer = Index('customer_sendtank')
customer.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@customer.doc_type
class CustomerDocument(DocType):
    full_name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    lists = fields.ObjectField(attr="get_grouped_lists", properties={
        'list_id': fields.IntegerField(),
        'list_data': fields.ObjectField(properties={
            'id': fields.IntegerField(),
            'name': fields.TextField()
        })
    })

    add_fields = fields.ObjectField()

    def prepare_add_fields(self, instance):
        return instance.add_fields

    #
    # def prepare_lists(self, instance):
    #     return [list.name for list in instance.lists.all()]

    class Meta:
        model = Customer
        # related_models = [List, ListCustomer, Company]
