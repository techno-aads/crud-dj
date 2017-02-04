from django.db import models
from django.utils.timezone import now


class TVShow(models.Model):
    name = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000)
    broadcasting_date = models.DateTimeField(default=now())
    contains_advertisement = models.BooleanField(default=False)

    def __str__(self):
        return self.name
