from django.db import models
from django.utils.timezone import now

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, default=now)
    updated = models.DateTimeField(auto_now=True, default=now)

    class Meta:
        abstract = True
