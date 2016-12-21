from django import forms

from .models import Programme


class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ('title', 'description', 'date', 'duration', 'isAd')

