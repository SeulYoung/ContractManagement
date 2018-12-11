import re

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.forms import LoginForm, RegistrationForm,UsernameForm,PasswordForm


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
                return render(request, 'login.html', {'form': form})
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


def email_update(request):
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
        User.objects.filter(email=request.user.email).update(email=email)
        return redirect('/login.html')

    return render(request, 'emailUpdate.html')


def password_update(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if not request.user.check_password(old_password):
            return render(request, 'passwordUpdate.html', {'password_error': 'invalid password.'})
        if len(password) < 6:
            return render(request, 'passwordUpdate.html', {'password_error': 'password too short.'})
        if password != password_confirmation:
            return render(request, 'passwordUpdate.html', {'password_error': 'password mismatch.'})
        request.user.set_password(password)
        request.user.save()
        return redirect('/login.html')

    return render(request, 'passwordUpdate.html')


def logout(request):
    auth.logout(request)
    return redirect('/landing')
