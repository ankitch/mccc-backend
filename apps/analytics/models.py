from django.db import models
from apps.analytics.signals import url_viewed_signal
from apps.tanks.models import Customer, Campaign
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


class ObjectViewed(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    short_url = models.ForeignKey(ShortenedUrl, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s viewed on   %s" % (self.customer.full_name, self.short_url.short_code, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Url Viewed'
        verbose_name_plural = 'Urls viewed'


def url_viewed_receiver(sender, cus, short, camp, request, *args, **kwargs):
    url_view = ObjectViewed(customer=cus, short_url=short, campaign=camp)
    url_view.save()


url_viewed_signal.connect(url_viewed_receiver)
