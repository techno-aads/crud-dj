from django.db import models
from django.utils import timezone

#Товары: 
#1)Название товара
#2)количество товара
#3)адрес доставки
#4)дата доставки
#5)статус

class Prod(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    num = models.CharField(max_length=200)
	#adres = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    status = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title