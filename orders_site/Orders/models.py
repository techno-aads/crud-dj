from django.db import models

# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class Order(models.Model):
	title = models.CharField(max_length=200)
	count = models.IntegerField(default=0)
	address = models.CharField(max_length=200)
	date = models.DateTimeField('date delivery')
	status = models.ForeignKey(Status,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
		
		
