from django.db import models

from django.utils import timezone


class Good(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=30)
    delivery_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


