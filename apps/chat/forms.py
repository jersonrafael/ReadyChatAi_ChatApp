from django.forms import ModelForm
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class message_form(ModelForm):
    class Meta:
        model = models.message
        fields = ['to','text']
        widgets = {
            'to': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'text': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control bg-indigo-400 outline-none border-b border-black"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')