from django.db import models


class SendFCMLog(models.Model):
    type = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
