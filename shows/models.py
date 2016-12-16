from django.db import models
from django.core.urlresolvers import reverse

class Show(models.Model):
    name = models.CharField(max_length=50)
    running_time = models.IntegerField(default=0) #in minutes
    description = models.CharField(max_length=250)
    run_date = models.DateTimeField('run date')
    has_ads = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shows:server_edit', kwargs={'pk': self.pk})
