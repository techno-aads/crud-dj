from __future__ import unicode_literals

from datetime import timedelta, datetime
from django.db import models

# Create your models here.

class tv_program(models.Model):
    name = models.CharField(max_length=100, default='name')
    duration = models.DurationField(default=timedelta())
    description = models.CharField(max_length=300, default='description')
    date_prog = models.DateTimeField(default=datetime.now, blank=True)
    commercials = models.BooleanField()
