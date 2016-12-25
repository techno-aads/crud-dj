from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    addres = models.CharField(max_length=100)
    date = models.DateField()
    status = models.BooleanField(default = False)
    
