from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory

from datetimewidget.widgets import DateWidget

class ItemForm(forms.Form):
	name = forms.CharField()
	amount = forms.IntegerField()
	address = forms.CharField()
	#delivery_time = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
	#status = forms.CharField()