from django.db import models

# Create your models here.

class Shows(models.Model):
    name = models.CharField(max_length=300, default='name')
    description = models.CharField(max_length=300, default='description')
    duration = models.IntegerField(default=60)
    date = models.CharField(max_length=50)
    hasAd = models.CharField(max_length=10, default='False')

    def __str__(self):
        return self.name