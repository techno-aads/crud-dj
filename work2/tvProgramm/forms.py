from django import forms
from .models import Programm
from django.core import validators
from django.contrib.auth.models import User

class AddProgrammForm(forms.ModelForm):
    class Meta:
        model = Programm
        fields = ['name', 'length', 'description', 'date', 'ad']
        widgets = {
            'length': forms.TimeInput(format='%H:%M'),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=100)
