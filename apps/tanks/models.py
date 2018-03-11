from django.contrib.postgres.fields import JSONField
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    add_fields = JSONField()
    lists = models.ManyToManyField(List, related_name='customers', through='ListCustomer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    #
    # add_fields
    # ": {
    # "age": "25",
    # "address": {
    #     "city": "Chirtwan",
    #     "country": "Nepal"
    # }}

    def jsonleaves(self):
       leaves = Leaf(self.add_fields)
       # print(leaves.text)
       return leaves.text
        # return ''.join(text)


class ListCustomer(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  - %s' % (self.list, self.customer)
    #
    # class Meta:
    #     auto_created = True


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='campaigns')
    emails = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    # #
    # class Meta:
    #     auto_created = True


class Leaf(object):
    def __init__(self, dictionary):
        self.text = ''
        self.rec(dictionary)
        # print(self.text)

    def rec(self, dic):
        for key, value in dic.items():
            if isinstance(value, dict):
                self.rec(value)
            elif isinstance(value, list):
                self.recl(value)
            else:
                # print(value)
                self.text += str(value) + ','

    def recl(self, lis):
        for item in lis:
            if isinstance(item, list):
                self.recl(item)
            elif isinstance(item, dict):
                self.rec(item)
            else:
                # print(item)
                self.text += str(item) + ','
