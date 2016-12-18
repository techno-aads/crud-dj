from django.db import models
from datetime import datetime, timezone

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    address = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return " ".join([self.name, str(self.quantity),
                         self.address, str(self.date) , str(self.status)])

    def publish(self):
        self.date = timezone.now()
        self.save()