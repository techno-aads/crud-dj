from django.db import models


class Telecast(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField(default=90)
    description = models.CharField(max_length=500)
    broadcastDate = models.DateTimeField()
    isAdvertising = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' ' + \
               self.description + ' ' + \
               str(self.duration) + ' ' + \
               str(self.broadcastDate) + ' ' + \
               str(self.isAdvertising)
