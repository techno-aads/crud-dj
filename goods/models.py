from django.db import models
from django.utils import timezone


class Order(models.Model):
    class Meta:
        db_table = 'order'

    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField(default=1)
    delivery_address = models.CharField(max_length=300)
    delivery_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    def deliver(self):
        if self.status is True:
            self.delivery_date = timezone.now()
            self.save()

    def __str__(self):
        return self.product_name
