from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=200)
    timeLen = models.IntegerField()
    description = models.CharField(max_length=400)
    dateTime = models.DateTimeField()
    ad = models.BooleanField()

    def __str__(self):
        return self.name
