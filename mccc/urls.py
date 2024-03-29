from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.analytics.api import DashboardAnalytics, SMSAnalyticsViewSet, CampaignAnalytics, MisscallAnalyticsViewSet, \
    CampaignMisscallAnalytics
from apps.send.api import SendSMS, ScheduleCampaign, PushDataMessage, SyncDataMessage, RepliesViewset, SendMessage
from apps.tanks import api as tank_api
from apps.tanks import views as tank_views
from apps.tanks.api import GetMessage, AddSegment, CustomerDocumentView, CampaignListView
from apps.url_shortner.api import ShortenedUrlViewSet
from apps.url_shortner.views import ShortRedirectView
from apps.users import api as user_api
from apps.users.views import FCMDeviceRegistration

router = DefaultRouter()

router.register('company', user_api.CompanyViewSet, base_name='company')
router.register('customers', tank_api.CustomerViewSet, base_name='customers')
router.register('lists', tank_api.ListViewSet, base_name='lists')
router.register('campaigns', tank_api.CampaignViewSet, base_name='campaign')
router.register('segments', tank_api.SegmentViewSet, base_name='segment')
router.register('shortenedurl', ShortenedUrlViewSet, base_name='shortenurl')
router.register('sms/analytics', SMSAnalyticsViewSet, base_name='sms_analytics')
router.register('miscall/analytics', MisscallAnalyticsViewSet, base_name='misscall_analytics')
router.register('replies', RepliesViewset, base_name='replies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('v1/api/login/', obtain_jwt_token),
    path('v1/users/reg_id/', FCMDeviceRegistration.as_view()),

    path('v1/dashboard/', DashboardAnalytics.as_view()),
    path('v1/misscall/', CampaignListView.as_view()),

    path('v1/schedule/campaign/', ScheduleCampaign.as_view()),

    path('v1/lists/segments/create/', AddSegment.as_view()),
    path('v1/lists/<int:pk>/export/customers/', tank_views.export_customers, name='export_customers'),
    path('v1/lists/<int:pk>/import/customers/', tank_views.import_customers, name='import_customers'),

    path('v1/campaigns/<int:pk>/segment/<int:segmentpk>/', GetMessage.as_view()),
    path('v1/search/<int:campaginpk>/segment/<int:segmentpk>/', CustomerDocumentView.as_view()),
    path('v1/send/sms/', SendSMS.as_view()),

    path('v1/push/misscall/', PushDataMessage.as_view()),
    path('v1/push/sms/', SendMessage.as_view()),
    path('v1/sync/data/', SyncDataMessage.as_view()),

    path('v1/camp/analytics/<int:campaign_id>/', CampaignAnalytics.as_view()),
    path('v1/camp/misscall/analytics/<int:campaign_id>/', CampaignMisscallAnalytics.as_view()),

    path('s/<slug:shortcode>/<int:camp_id>/', ShortRedirectView.as_view())
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('debug', include(debug_toolbar.urls)), ] + urlpatterns
