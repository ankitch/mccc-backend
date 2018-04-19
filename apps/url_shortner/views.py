from django.http import HttpResponse
from django.views import View

from apps.url_shortner.models import ShortenedUrl


# Create your views here.


def short_url_redirect(request, shortcode=None, *args, **kwargs):
    print(shortcode)
    obj = ShortenedUrl.objects.get(short_code=shortcode)
    print(obj)
    return HttpResponse("hello {sc}".format(sc=obj.url))


class ShortRedirectView(View):
    def get(self, request, *args, shortcode=None, **kwargs):
        return HttpResponse("hello again")
