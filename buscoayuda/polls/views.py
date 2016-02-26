# coding=utf-8
import datetime

import boto
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Trabajador, TrabajadorForm, UserForm
from .models import TiposDeServicio
from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth


def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)
    context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador, 'form_usuario': form_usuario}
    return render(request, 'polls/index.html', context)


def login(request):
    username = request.POST.get('usrname', '')
    password = request.POST.get('psw', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Bienvenido al sistema {}".format(username), extra_tags="alert-success")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
        return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        trabajador_form = TrabajadorForm(data=request.POST)
        user = User()
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.is_superuser = False
        user.username = request.POST.get('username') + '3'
        user.email = request.POST.get('correo')
        user.is_staff = False
        user.is_active = True
        user.date_joined = datetime.datetime.now()
        user.save()
        user.set_password(request.POST.get('password'))
        trabajador = trabajador_form.save(commit=False)
        if trabajador.is_valid():
            trabajador.user = user
            trabajador.save()
    return HttpResponseRedirect('/')
