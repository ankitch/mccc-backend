from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.analytics.api import DashboardAnalytics, SMSAnalyticsViewSet
from apps.send.api import SendSMS, ScheduleCampaign
from apps.tanks import api as tank_api
from apps.tanks import views as tank_views
from apps.tanks.api import Settings, GetMessage, AddSegment
from apps.tanks.haystack_api import CustomerSearchView
from apps.url_shortner.api import ShortenedUrlViewSet
from apps.url_shortner.views import ShortRedirectView
from apps.users.views import FCMDeviceRegistration

router = DefaultRouter()

router.register('customers', tank_api.CustomerViewSet, base_name='customers')
router.register('lists', tank_api.ListViewSet, base_name='lists')
router.register('campaigns', tank_api.CampaignViewSet, base_name='campaign')
router.register('segments', tank_api.SegmentViewSet, base_name='segment')
router.register('shortenedurl', ShortenedUrlViewSet, base_name='shortenurl')
router.register('sms/analytics', SMSAnalyticsViewSet, base_name='sms_analytics')
router.register('customer/search', CustomerSearchView, base_name='customer_search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/dashboard/', DashboardAnalytics.as_view()),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('v1/users/reg_id/', FCMDeviceRegistration.as_view()),
    path('v1/send/sms/', SendSMS.as_view()),

    path('v1/schedule/campaign/', ScheduleCampaign.as_view()),

    path('v1/lists/<int:pk>/export/customers/', tank_views.export_customers, name='export_customers'),

    path('v1/lists/<int:pk>/import/customers/', tank_views.import_customers, name='import_customers'),

    path('v1/lists/segments/create/', AddSegment.as_view()),
    path('v1/campaigns/<int:pk>/segment/<int:segmentpk>/', GetMessage.as_view()),

    path('v1/settings/', Settings.as_view()),
    path('s/<slug:shortcode>/<int:camp_id>/', ShortRedirectView.as_view())
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('debug', include(debug_toolbar.urls)), ] + urlpatterns
