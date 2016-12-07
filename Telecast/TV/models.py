from __future__ import unicode_literals

from django.db import models


class TV(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    duration = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    advert = models.BooleanField(default=0)

    def __str__(self):
        return self.name
