from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Programme(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    description = models.TextField(max_length=500)
    date = models.DateTimeField()
    isAd = models.BooleanField(default=True)

    def __str__(self):
        return self.title
