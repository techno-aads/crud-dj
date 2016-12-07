from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=200)
    timeLen = models.IntegerField()
    description = models.CharField(max_length=400)
    dateTime = models.CharField(max_length=200)
    ad = models.CharField(max_length=200)

    def __str__(self):
        return self.name
