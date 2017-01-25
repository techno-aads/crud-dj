from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'johndoe'}), help_text="Enter desired username (not more than 30 symbols)")
    password1 = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}), help_text="Enter desired password (8 or more symbols)")
    password2 = forms.CharField(label="Password confirmation", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}), help_text="Enter the same password as before, for verification")
