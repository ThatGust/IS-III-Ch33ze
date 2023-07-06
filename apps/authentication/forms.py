# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TeacherForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombres",
                "class": "form-control"
            }
        ))
    apellidos = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "apellidos",
                "class": "form-control"
            }
        ))
    mail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "mail",
                "class": "form-control"
            }
        ))
    cui = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "cui",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "address",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "city",
                "class": "form-control"
            }
        ))
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "country",
                "class": "form-control"
            }
        ))
    

class StudentForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "nombres",
                "class": "form-control"
            }
        ))
    apellidos = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "apellidos",
                "class": "form-control"
            }
        ))
    mail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "mail",
                "class": "form-control"
            }
        ))
    cui = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "cui",
                "class": "form-control"
            }
        ))
    course = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "course",
                "class": "form-control"
            }
        ))