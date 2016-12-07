from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DecimalField(decimal_places=0, max_digits=200)
    discription = models.CharField(max_length=200)
    show_date = models.CharField(max_length=50)
    adds = models.CharField(max_length=3)

    def __str__(self):
        return self.name
