from django.contrib import auth
from django.shortcuts import render, redirect

from app.forms import *


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
                    return redirect('/profile.html')
            else:
                form.add_error('password', '密码错误')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            User.objects.create_user(username=username, password=password)

            return redirect('/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        info = User.objects.filter(username=request.user.username).first()
        return render(request, 'profile.html', {'username': info.username})
    return redirect('/login.html')


def username_update(request):
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            User.objects.filter(username=username).update(username=username)
            return redirect('/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'UsernameUpdate.html', {'form': form})


def password_update(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            password = form.cleaned_data['password2']

            if request.user.check_password(old_password):
                request.user.set_password(password)
                request.user.save()
                return redirect('/login.html')
            else:
                form.add_error('password', '密码错误')
    else:
        form = RegistrationForm()
    return render(request, 'PasswordUpdate.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/landing')
