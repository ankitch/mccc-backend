from django.conf import settings
from django.db import models

from .utils import create_short_code

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class ShortenedUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortenedUrlManager, self).all(*args, **kwargs)
        qs = qs.filter(active=False)
        return qs

    def refresh_shortcode(self, items=10):
        print(items)
        qs = ShortenedUrl.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.short_code = create_short_code(q)
            print(q.id)
            q.save()
            new_code += 1
        return "New code made {i}".format(i=new_code)


class ShortenedUrl(models.Model):
    url = models.CharField(max_length=256)
    short_code = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortenedUrlManager()

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = create_short_code(self)
        super(ShortenedUrl, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
