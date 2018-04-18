from django.db import models

from .utils import short_code_generator


class ShortenedUrl(models.Model):
    url = models.CharField(max_length=256)
    short_code = models.CharField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = short_code_generator()
        super(ShortenedUrl, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
