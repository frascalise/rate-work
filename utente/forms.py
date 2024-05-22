from django import forms
from .models import Utente
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label='Password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.CharField(
        label='Email', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    nome = forms.CharField(
        label='Nome', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='Password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Ripeti password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Utente
        fields = ('username', 'email', 'nome', 'password1', 'password2', 'is_azienda')
