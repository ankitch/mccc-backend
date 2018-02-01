from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')

admin.site.register(Customer, CustomerAdmin)
