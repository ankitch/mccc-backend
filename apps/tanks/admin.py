from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Customer, List, Campaign, ListCustomer, Segments, SegmentList, SettingConfig


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')


admin.site.register(ListCustomer)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SettingConfig, SingletonModelAdmin)
admin.site.register(List)
admin.site.register(Campaign)
admin.site.register(Segments)
admin.site.register(SegmentList)
