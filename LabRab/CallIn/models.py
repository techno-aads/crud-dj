import datetime

from django.db import models
from django.utils import timezone

class Telecast(models.Model):
    tel_name = models.CharField(max_length=20)
    tel_duration = models.IntegerField(default = 60)
    tel_descr = models.CharField(max_length=200)
    tel_date = models.DateTimeField(default= timezone.now() )
    tel_adv_op = models.BooleanField(default=1)
    def __str__(self):
        return self.tel_name
    def was_pub(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.tel_date <= now

