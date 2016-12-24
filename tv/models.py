from django.db import models


# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    length = models.PositiveIntegerField()
    date = models.DateField()
    add_advert = models.BooleanField()

    def __str__(self):
        return self.name
