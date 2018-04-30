from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

# Create your views here.
from apps.analytics.models import ClickEvent
from apps.analytics.signals import url_viewed_signal
from apps.tanks.models import Customer, Campaign
from .models import ShortenedUrl

#
# def short_url_redirect(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(ShortenedUrl, short_code=shortcode)
#     return HttpResponseRedirect(obj.url)


class ShortRedirectView(View):

    def get(self, request, *args, cus_id=None, shortcode=None, camp_id=None, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        short = get_object_or_404(ShortenedUrl, short_code=shortcode)
        cus = get_object_or_404(Customer, id=cus_id)
        camp = get_object_or_404(Campaign, id=camp_id)
        # ClickEvent.objects.create_event(short)
        url_viewed_signal.send(sender=short.__class__, cus=cus, short=short, camp=camp, request=request)
        # ClickEvent.objects.add_person(cus)
        return HttpResponseRedirect(short.url)
