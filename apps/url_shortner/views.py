from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from apps.analytics.models import ClickEvent
from .models import ShortenedUrl


class ShortRedirectView(View):
    def get(self, request, *args, shortcode=None, camp_id=None, **kwargs):
        obj = get_object_or_404(ShortenedUrl, short_code=shortcode)
        ClickEvent.objects.create_event(obj)

        return HttpResponseRedirect(obj.url)
