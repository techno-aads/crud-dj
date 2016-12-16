from django import forms
from .models import Programm

class AddProgrammForm(forms.ModelForm):
    class Meta:
        model = Programm
        fields = ['name', 'length', 'description', 'date', 'ad']
        widgets = {
            'length': forms.TimeInput(format='%H:%M'),
        }
        