from haystack import indexes

from .models import Customer


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    email = indexes.CharField(model_attr='email')
    phone = indexes.CharField(model_attr='phone')
    fcm_id = indexes.CharField(model_attr='fcm_id', default=None)
    age = indexes.CharField()
    sex = indexes.CharField()
    lists = indexes.MultiValueField(indexed=True, stored=True)

    def prepare_age(self, obj):
        return obj.add_fields['age']

    def prepare_sex(self, obj):
        return obj.add_fields['sex']

    def prepare_lists(self, obj):
        return [list.name for list in obj.lists.all()]
    

    def get_model(self):
        return Customer
