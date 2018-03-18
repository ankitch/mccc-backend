from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.send.api import send_email
from apps.tanks import api as tank_api
from apps.tanks.api import grape_mail_load
from apps.tanks.haystack_api import CustomerSearchView

router = DefaultRouter()


router.register('customers',tank_api.CustomerViewSet)
router.register('lists',tank_api.ListViewSet)
router.register('campaigns', tank_api.CampaignViewSet)
router.register('settings', tank_api.SettingsViewSet)
router.register('customer/search', CustomerSearchView, base_name='customer-search')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include(router.urls)),
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/campaigns/email/<int:pk>/', grape_mail_load),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('v1/send/email', send_email),
    path('search/', include('haystack.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('debug', include(debug_toolbar.urls)), ] + urlpatterns
