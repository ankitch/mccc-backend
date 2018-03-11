from haystack import indexes
from .models import Customer
from .models import Settings


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    email = indexes.CharField(model_attr='email')

    # add_fields = indexes.CharField(model_attr='add_fields')

    def prepare(self, obj):
        data = super().prepare(obj)
        # data['add_fields'] = obj.add_fields
        for key,value in obj.add_fields.items():
            data[key] = value
        return data

    def get_model(self):
        return Customer

    # def rec(self, dic):
    #     json = {}
    #     for key, value in dic.items():
    #         if isinstance(value, dict):
    #             self.rec(value)
    #     # elif isinstance(value, list):
    #     #     self.recl(value)
    #         else:
    #             # print(value)
    #             json[key] = value
    #             # print(key, value)
    #             return(json)
