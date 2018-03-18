from haystack import indexes

from .models import Customer
from .models import Settings


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    email = indexes.CharField(model_attr='email')
    phone = indexes.CharField(model_attr='phone')
    fcm_id = indexes.CharField(model_attr='fcm_id')
    age = indexes.CharField()
    sex = indexes.CharField()
    lists = indexes.MultiValueField(indexed=True, stored=True)

    def prepare_age(self,obj):
        return obj.add_fields['age']

    def prepare_sex(self, obj):
        return obj.add_fields['sex']

    def prepare_lists(self, obj):
        return [list.name for list in obj.lists.all()]

    # query = {'age': '18', 'sex': 'female'}
    # smth = Customer.objects.all().values_list('add_fields')
    # print(list(smth))
    # for item in list(smth):
    #     print(item)
    # #     print(type(item))
    # add_fields = indexes.CharField(model_attr='add_fields')

    # def prepare(self, obj):
    #     data = super(CustomerIndex, self).prepare(obj)
    #     # print(obj.email)
    #     # data['add_fields'] = obj.add_fields
    #     for key, value in obj.add_fields.items():
    #         data[key] = value
    #     return data

    def get_model(self):
        return Customer

    # def do(self, value):
    #     age = indexes.CharField(de)
