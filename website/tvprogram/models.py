from django.db import models
from django.utils import timezone


class TVShow(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    broadcasting_date = models.DateTimeField(default=timezone.now())
    contains_advertisement = models.BooleanField(default=False)

    def __str__(self):
        return self.name
