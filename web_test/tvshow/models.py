from __future__ import unicode_literals

from datetime import datetime

from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.




@python_2_unicode_compatible  # only if you need to support Python 2
class Show(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    description = models.CharField(max_length=500)
    broadcast_date = models.DateField()
    advert = models.CharField(max_length=3)

    def __str__(self):
        return self.name
