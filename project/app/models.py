from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	count = models.IntegerField(default=0)
	address = models.CharField(max_length=400)
	delivery_date = models.DateField(null=True)
	status = models.BooleanField(default=False)
	def __str__(self):
		return self.name
