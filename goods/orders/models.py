from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=77)
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    delivery_date = models.DateTimeField('delivery date')
    status = models.BooleanField()

    def __str__(self):
        return self.name