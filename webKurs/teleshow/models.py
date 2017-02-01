from django.db import models
from django.utils import timezone

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    broadcast_date = models.DateTimeField(default=timezone.now)
    advertisement = models.BooleanField(default=False)
    def __str__(self):
        return self.name
