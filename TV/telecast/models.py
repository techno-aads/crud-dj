from django.db import models

class Question(models.Model):
	telecast_text = models.CharField(max_length=200)
	telecast_length = models.IntegerField(default=0)
	telecast_data = models.DateTimeField('date published')
	telecast_description = models.CharField(max_length=200)
	spam_on_off = (
		('ON', 'on'),
		('OFF', 'off'),
	)
