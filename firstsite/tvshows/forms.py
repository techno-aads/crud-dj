from django import forms

class ShowForm(forms.Form):
    name = forms.CharField(max_length=100)
    broadcast_date = forms.DateField()
    time = forms.TimeField()
    description = forms.CharField(max_length=500)
    advert = forms.CharField(max_length=3)