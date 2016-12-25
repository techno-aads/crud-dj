from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.

class TVPrograms(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    duration = models.TimeField(default=timezone.now)
    date = models.DateField(default=date.today)
    advert = models.BooleanField(default=False)

    def __str__(self):
        return self.name
