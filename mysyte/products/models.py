from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    delivery_date = models.DateTimeField('date published')
    status = models.BooleanField(default=False)

    def __str__(self):
        return "name=" + self.name + " " \
        "count=" + str(self.count) + " " \
        "address=" + self.address + " " \
        "delivery_date=" + str(self.delivery_date) + " " \
        "status=" + str(self.status)