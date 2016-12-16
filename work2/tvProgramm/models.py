from django.db import models
from django.forms import ModelForm

# Create your models here.

class Programm(models.Model):
    name = models.CharField(max_length=200)
    length = models.TimeField()
    description = models.CharField(max_length=300)
    date = models.DateField()
    ad = models.BooleanField(blank=True)
    

    def __str__(self):
        return self.name

class DeleteProgrammForm(ModelForm):
    class Meta:
        model = Programm
        fields = []
    