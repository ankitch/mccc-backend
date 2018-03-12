from haystack import indexes
from .models import Customer
from .models import Settings


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    email = indexes.CharField(model_attr='email')
    phone = indexes.CharField(model_attr='phone')

    # add_fields = indexes.CharField(model_attr='add_fields')

    def prepare(self, obj):
        data = super().prepare(obj)
        # data['add_fields'] = obj.add_fields
        for key,value in obj.add_fields.items():
            data[key] = value
        return data

    def get_model(self):
        return Customer
