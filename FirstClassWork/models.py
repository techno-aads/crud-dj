from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    to = models.CharField(max_length=100) #куда доставляем
    date = models.DateField()
    complete = models.BooleanField(default = False)
    
