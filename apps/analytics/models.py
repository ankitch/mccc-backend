from django.db import models
from apps.tanks.models import Customer
from apps.url_shortner.models import ShortenedUrl


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortenedUrl):
            obj, created = self.get_or_create(short_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    customers = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    short_url = models.OneToOneField(ShortenedUrl, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    visit_time = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
