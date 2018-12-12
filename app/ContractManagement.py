from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

from django.shortcuts import render, redirect

from app.forms import LoginForm, RegistrationForm, UsernameForm, PasswordForm


def C_Select(request):
    return render(request,'Contract_select.html')