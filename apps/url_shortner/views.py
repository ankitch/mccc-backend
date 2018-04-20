from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

# Create your views here.
from apps.analytics.models import ClickEvent
from .models import ShortenedUrl

#
# def short_url_redirect(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(ShortenedUrl, short_code=shortcode)
#     return HttpResponseRedirect(obj.url)


class ShortRedirectView(View):
    def get(self, request, *args, shortcode=None, **kwargs):
        obj = get_object_or_404(ShortenedUrl, short_code=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)
