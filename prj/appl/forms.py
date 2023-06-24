from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Register(UserCreationForm):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={
        "class":"form-control"
    }))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={
        "class":"form-control"
    }))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "id":"Rpassword"
    }))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class":"form-control"
    }))


    class Meta:
        model = User
        fields = ["username",'email', 'password1','password2']

class Login(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        "class":"form-control",
        'autocomplete': 'on'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class":"form-control",
        'autocomplete': 'on',
        'id':'Lpassword'
    }))