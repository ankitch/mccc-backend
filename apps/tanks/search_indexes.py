from haystack import indexes
from .models import Customer


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    # add_fields = indexes.CharField(model_attr='add_fields')

    def get_model(self):
        return Customer
