from django.contrib import admin

from apps.users.models import Company
from .models import Customer, List, Campaign, ListCustomer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')


admin.site.register(ListCustomer)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(List)
admin.site.register(Campaign)
admin.site.register(Company)
