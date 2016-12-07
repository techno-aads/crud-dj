import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Student(models.Model):
    learnSubj = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.family
