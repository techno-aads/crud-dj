from __future__ import unicode_literals

from django.db import models



class Item(models.Model):
	name = models.CharField(max_length=200)
	amount = models.IntegerField(default=1)
	address = models.CharField(max_length=200)
	#delivery_time = models.DateTimeField('delivery time')
	#status = models.CharField(max_length=20, default='delivering')

	def __str__(self):
		return self.name


