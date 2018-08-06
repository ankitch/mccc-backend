from django.db import models

#
# class SendFCMLog(models.Model):
#     type = models.CharField(max_length=30)
#     status = models.CharField(max_length=30)
#     timestamp = models.DateTimeField(auto_now_add=True)
from apps.users.models import Company

STATUS = (
    ('Sent', 'Sent'),
    ('Delivered', 'Delivered'),
)

# models for storing message
class Replies(models.Model):
    mobile_number = models.CharField(max_length=30)
    message = models.CharField(max_length=160)
    timestamp = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.mobile_number
