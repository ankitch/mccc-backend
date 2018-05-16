from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View
from apps.analytics.signals import url_viewed_signal
from apps.tanks.models import Customer, Campaign
from .models import ShortenedUrl


class ShortRedirectView(View):
    def get(self, request, *args, cus_id=None, shortcode=None, camp_id=None, **kwargs):
        short = get_object_or_404(ShortenedUrl, short_code=shortcode)
        customer = get_object_or_404(Customer, id=cus_id)
        campaign = get_object_or_404(Campaign, id=camp_id)

        url_viewed_signal.send(sender=short.__class__, cus=customer, short=short, camp=campaign, request=request)

        return HttpResponseRedirect(short.url)
