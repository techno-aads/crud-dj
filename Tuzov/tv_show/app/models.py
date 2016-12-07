from django.db import models
from datetime import datetime

class TVShow(models.Model):
    name = models.CharField(max_length = 200)
    duration = models.IntegerField(default = 0)
    description = models.CharField(default = '', max_length = 10000)
    broadcast_date = models.DateTimeField(default=datetime.now)
    advertisement = models.BooleanField(default = False)

    def __str__(self):
        return self.name
