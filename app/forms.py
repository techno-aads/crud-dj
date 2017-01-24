from django import forms
from django.forms import ModelForm
from .models import tv_program

class DateInput(forms.DateInput):
    input_type = 'date'

class EditForm(ModelForm):
    # name = forms.CharField(max_length=100)
    # duration = forms.DurationField()
    # description = forms.CharField(max_length=300)
    # date_prog = forms.DateTimeField()
    # options = forms.BooleanField()
    class Meta:
        model = tv_program
        fields = ['name', 'duration', 'description', 'date_prog', 'commercials']
        widgets ={
            'date_prog': DateInput(),
        }
