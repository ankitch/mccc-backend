from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Customer, List, Campaign, ListCustomer, Segment, SegmentList, SettingConfig


# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('company')


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'list', 'company')
    search_fields = ('name', 'list__name', 'list__company__name')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('list__company')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')


admin.site.register(ListCustomer)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SettingConfig, SingletonModelAdmin)
admin.site.register(List)
admin.site.register(Campaign)
admin.site.register(Segment)
admin.site.register(SegmentList)
