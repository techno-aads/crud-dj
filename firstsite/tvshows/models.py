from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    description = models.CharField(max_length=500)
    broadcast_date = models.DateField()
    advert = models.CharField(max_length=3)

    def __str__(self):
        return self.name
