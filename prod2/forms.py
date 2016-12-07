from django import forms
from .models import Prod


class ProdForm(forms.ModelForm):
    class Meta:
        model = Prod
        fields = ('title', 'num', 'date', 'adress', 'status')
