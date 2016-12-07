import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=300)
    count = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    isArrive = models.CharField(max_length=10, default='False')

    def __str__(self):
        return self.name