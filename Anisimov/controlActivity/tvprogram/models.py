from django.db import models
from django.utils import timezone

# Create your models here.
class Tvprogram(models.Model):
    #Название телепередачи
    title = models.CharField(max_length = 200)
    #Длительность телепередачи
    duration = models.IntegerField(default=0)
    #Описание телепередачи
    description = models.CharField(max_length = 400)
    #Дата трансляции
    date = models.DateTimeField()
    #Опции реклами
    ADV_CHOICES = (
        (u'Y', u'Advertisement(Commercial)'),
        (u'N', u'No advertisement(Non commercial)'),
    )
    adv_option = models.CharField(max_length = 2, choices = ADV_CHOICES)
    def __str__(self):
        return self.title
