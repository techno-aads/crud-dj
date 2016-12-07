from django.db import models
from datetime import date


class Telecast(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField(default=90)
    description = models.CharField(max_length=500)
    broadcastDate = models.DateField(default=date.today)
    isAdvertising = models.BooleanField(default=False)
