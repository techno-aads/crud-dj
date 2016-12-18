from django.db import models
from django.forms import ModelForm
from django import forms

class Show(models.Model):
    name = models.CharField(max_length=50)
    running_time = models.IntegerField(default=0) #in minutes
    description = models.CharField(max_length=250)
    run_date = models.DateTimeField('run date')
    has_ads = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ShowForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "In Bruges"}))
    running_time = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "107"}), help_text="In minutes")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "In Bruges is a 2008 British/American black comedy crime film written and directed by Martin McDonagh."}))
    run_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':"2016-12-10 16:00:00"}), help_text="Format: YYYY-MM-DD HH:MM:SS (ex: 2016-12-10 16:00:00)")

    class Meta:
        model = Show
        fields = '__all__'