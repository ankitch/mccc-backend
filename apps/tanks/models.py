from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

from apps.url_shortner.models import ShortenedUrl
from apps.users.models import Company


class List(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    fcm_id = models.CharField(max_length=300, blank=True, null=True, default=None)
    add_fields = JSONField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers')
    lists = models.ManyToManyField(List, through='ListCustomer', related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class ListCustomer(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  - %s' % (self.list, self.customer)

    # class Meta:
    #     auto_created = True


CAMPAIGN_TYPE = (
    ('Bulk', 'Bulk'),
    ('Regular', 'Regular'),
    ('Misscall', 'Misscall')
)


class Campaign(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    details = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=CAMPAIGN_TYPE)
    to_numbers = ArrayField(models.CharField(max_length=20, blank=True, null=True), blank=True, null=True)
    sms_template = models.TextField(blank=True, max_length=160)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='campaigns', blank=True, null=True)
    short_url = models.ForeignKey(ShortenedUrl, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    misscall_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.misscall_active:
            try:
                temp = Campaign.objects.get(misscall_active=True)
                if self != temp:
                    temp.misscall_active = False
                    temp.save()
            except Campaign.DoesNotExist:
                pass

        # old = Campaign.objects.get(pk=self.id)
        # if old:
        #     if old.sms_template != self.sms_template:
        #         print("changed")
        super(Campaign, self).save(*args, **kwargs)

    def company_name(self):
        return self.company.name

    def __str__(self):
        return self.name


class Segment(models.Model):
    name = models.CharField(max_length=255)
    query = JSONField()
    lists = models.ManyToManyField(List, related_name='segments', through='SegmentList')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='segments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SegmentList(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    segments = models.ForeignKey(Segment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s  - %s' % (self.list, self.segments)

    # class Meta:
    #     auto_created = True
