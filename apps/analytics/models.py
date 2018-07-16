from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.tanks.models import Campaign
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
    short_url = models.OneToOneField(ShortenedUrl, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    visit_time = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)


class SMSAnalytics(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    sent = ArrayField(models.CharField(max_length=10, null=True), null=True,
                      blank=True)
    delivered = ArrayField(models.CharField(max_length=10, null=True), null=True, blank=True)
    timestamp = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.name

    @property
    def campaign_name(self):
        return self.campaign.name


class MisscallAnalytics(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20, null=True)
    timestamp = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.name + " " + self.mobile_number

    @property
    def campaign_name(self):
        return self.campaign.name
