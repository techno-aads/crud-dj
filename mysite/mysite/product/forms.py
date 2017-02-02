from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

from .models import InfoProd

class ProdForm(forms.ModelForm):

    class Meta:
       model = InfoProd
       fields = ('prod_title', 'prod_count', 'prod_address', 'prod_date', 'prod_status')

