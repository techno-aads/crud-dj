from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	login = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	isAbleToEdit = models.BooleanField(default = False)
	def __str__(self):
		res = self.login + " - "
		if self.isAbleToEdit == True:
			res += 'admin'
		else:
			res += 'user'
		return res
