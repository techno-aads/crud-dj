from django import forms
from django.contrib.auth.models import User

from .models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'timeLen', 'description', 'dateTime', 'ad',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
