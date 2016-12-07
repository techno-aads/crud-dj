from django.db import models

# Create your models here.
class Order(models.Model):
	name = models.CharField(max_length=20)
	amount = models.IntegerField(default = 0)
	addres = models.CharField(max_length=50)
	date = models.DateTimeField('date published')
	status = models.BooleanField(default='false')