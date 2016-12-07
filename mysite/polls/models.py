from django.db import models

import datetime
from django.utils import timezone
from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    date = models.DateField(default='2016-12-06')
    status = models.BooleanField(default=False)

    def was_ordered_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    def __str__(self):
        stat = " "
        if (self.status == True):
            stat="Выполнен"
        else:
                stat="Не выполнен"
        return "Название товара: " + self.product_name + ", Количество товара: " + str(self.quantity) + ", Адрес доставки: " + self.address + ", Дата заказа: " + str(self.date) + ", Статус заказа: " + str(stat)