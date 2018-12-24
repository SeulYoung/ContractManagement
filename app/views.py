from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect

from app.forms import *
from app.models import *


class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(Q(username=username) | Q(email=username))
        if user.check_password(password):
            return user


def landing(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/profile')
            else:
                form.add_error('password', '密码错误')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('/login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user.username).first()
        permission = 'None'
        right = Right.objects.filter(userName=request.user.username).first()
        if right is not None:
            role = Role.objects.filter(name=right.roleName).first()
            permission = role.functions
        return render(request, 'profile.html', {'user': user, 'permission': permission})
    return redirect('/login')


def email_update(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if request.user.check_password(password):
                User.objects.filter(username=request.user.username).update(email=email)
                return redirect('/profile')
            else:
                form.add_error('password', '密码错误')
    else:
        form = RegistrationForm()
    return render(request, 'emailUpdate.html', {'form': form})


def password_update(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            password = form.cleaned_data['password2']
            if request.user.check_password(old_password):
                request.user.set_password(password)
                request.user.save()
                return redirect('/login')
            else:
                form.add_error('old_password', '原密码错误')
    else:
        form = RegistrationForm()
    return render(request, 'passwordUpdate.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')
