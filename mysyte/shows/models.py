from django.db import models
from django.forms import ModelForm
from django import forms


class Show(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DecimalField(decimal_places=0, max_digits=200)
    description = models.CharField(max_length=200)
    show_date = models.DateTimeField('date published')
    adds = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class ShowForm(ModelForm):
    duration = forms.DecimalField(min_value=1, max_value=200)
    show_date = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Show
        fields = "__all__"
