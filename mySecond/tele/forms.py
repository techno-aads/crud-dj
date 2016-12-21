from django import forms
from .models import Television


class TelevisionForm(forms.ModelForm):
    class Meta:
        model = Television
        fields = ('name', 'time', 'description','date')