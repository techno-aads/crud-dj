from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory

from datetimewidget.widgets import DateWidget

from django.core import validators
from django.contrib.auth.models import User

class ItemForm(forms.Form):
	name = forms.CharField()
	amount = forms.IntegerField()
	address = forms.CharField()
	#delivery_time = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
	#status = forms.CharField()

class UserLoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=100)