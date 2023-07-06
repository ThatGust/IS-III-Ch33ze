# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, TeacherForm, StudentForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'El form no es valido'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True


        else:
            msg = 'El form no es valido'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def teacher_add(request):
    msg = None
    success = False

    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            nombres = form.cleaned_data.get("username")
            apellidos = form.cleaned_data.get("password1")
            mail = form.cleaned_data.get("passw ord1")
            cui = form.cleaned_data.get("password1")
            city = form.cleaned_data.get("password1")
            country = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=raw_password)

            msg = 'Docente registrado'
            success = True

        else:
            msg = 'El form no es valido'
    else:
        form = TeacherForm()

def student_add(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            nombres = form.cleaned_data.get("nombres")
            apellidos = form.cleaned_data.get("apellidos")
            mail = form.cleaned_data.get("mail")
            cui = form.cleaned_data.get("cui")
            course = form.cleaned_data.get("city")
            user = authenticate(username=username, password=raw_password)

            msg = 'Estudiante registrado'
            success = True

        else:
            msg = 'El form no es valido'
    else:
        form = StudentForm()