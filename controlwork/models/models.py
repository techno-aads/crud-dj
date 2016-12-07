from django.db import models

# Create your models here.

class Order(models.Model):
	name = models.CharField(max_length = 100)
	count = models.IntegerField(default=0)
	address = models.CharField(max_length = 150)
	order_date = models.DateTimeField('date published');
	state = models.BooleanField(default=False)
	def __str__(self):
		return self.id.__str__() +' '+self.name+', '+self.address