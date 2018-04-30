from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from apps.analytics.api import ObjectViewSet
from apps.send.api import send_push, send_sms, schedule_campaign, email_view
from apps.tanks import api as tank_api
from apps.tanks import views as tank_views
from apps.tanks.api import grape_mail_load
from apps.tanks.haystack_api import CustomerSearchView
from apps.url_shortner.views import ShortRedirectView

router = DefaultRouter()

router.register('customers', tank_api.CustomerViewSet)
router.register('lists', tank_api.ListViewSet)
router.register('campaigns', tank_api.CampaignViewSet)
router.register('segments', tank_api.SegmentViewSet)
router.register('customer/search', CustomerSearchView, base_name='customer-search')
router.register('analytics', ObjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/campaigns/email/<int:pk>/', grape_mail_load),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    path('v1/send/email', email_view),
    path('v1/send/push/', send_push),
    path('v1/send/sms/', send_sms),

    path('v1/schedule/campaign/', schedule_campaign),

    path('v1/lists/<int:pk>/export/customers/', tank_views.export_customers, name='export-customers'),
    path('v1/lists/<int:pk>/import/customers/', tank_views.import_customers, name='import_customers'),

    path('v1/lists/segments/create/', tank_api.create_list_segment, name='list_segment'),
    path('v1/campaigns/<int:pk>/segment/<int:segmentpk>/', tank_api.segment, name='segment-customers'),
    path('v1/settings/', tank_api.create_settings, name="settings"),

    re_path(r'^s1/(?P<shortcode>[\w-]+)/(?P<cus_id>[\d+])/$', ShortRedirectView.as_view(), name='short_code')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('debug', include(debug_toolbar.urls)), ] + urlpatterns
