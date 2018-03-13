"""mccc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
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
    path('search/', include('haystack.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('debug', include(debug_toolbar.urls)), ] + urlpatterns
