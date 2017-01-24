from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class MyRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'placeholder': 'Login'
            })
        self.fields['first_name'].widget.attrs.update({
                'placeholder': 'First name'
            })
        self.fields['last_name'].widget.attrs.update({
                'placeholder': 'Last name'
            })
        self.fields['password1'].widget.attrs.update({
                'placeholder': 'Password'
            })
        self.fields['password2'].widget.attrs.update({
                'placeholder': 'Confirm password'
            })
        self.fields['email'].widget.attrs.update({
                'placeholder': 'E-mail'
            })
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user