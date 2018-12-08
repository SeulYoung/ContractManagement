import re

from django.contrib import auth
from django.shortcuts import render, redirect
from app.models import MyUser


def landing(request):
    if request.user.is_authenticated:
        return redirect('/profile.html')
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/profile.html')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        info = MyUser.objects.filter(email=email).first()
        if info is None:
            return render(request, 'login.html', {'login_error': 'email not found.'})
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/profile.html')
        else:
            return render(request, 'login.html', {'login_error': 'password is invalid.'})

    return render(request, 'login.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/profile.html')
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        email_valid = r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$'
        if not re.match(email_valid, email):
            return render(request, 'registration.html', {'registration_error': 'enter a valid email address.'})
        username_valid = r'^[a-z]+$'
        if not re.match(username_valid, username):
            return render(request, 'registration.html', {'registration_error': 'username has illegal characters.'})
        if len(password) < 6:
            return render(request, 'registration.html', {'registration_error': 'password too short.'})
        if password != password_confirmation:
            return render(request, 'registration.html', {'registration_error': 'password mismatch.'})

        info = MyUser.objects.filter(email=email).first()
        if info is not None:
            return render(request, 'registration.html', {'registration_error': 'email already taken.'})
        info = MyUser.objects.filter(username=username).first()
        if info is not None:
            return render(request, 'registration.html', {'registration_error': 'username already taken.'})
        MyUser.objects.create_user(email=email, username=username, password=password)

        return redirect('/login.html')
    return render(request, 'registration.html')


def profile(request):
    if request.user.is_authenticated:
        info = MyUser.objects.filter(email=request.user.email).first()
        return render(request, 'profile.html', {'email': info.email, 'username': info.username})
    return redirect('/login.html')


def email_update(request):
    if request.method == "POST":
        email = request.POST.get('email')
        email_valid = r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$'

        if not re.match(email_valid, email):
            return render(request, 'emailUpdate.html', {'email_error': 'enter a valid email address.'})
        info = MyUser.objects.filter(email=email).first()
        if info is not None:
            return render(request, 'emailUpdate.html', {'email_error': 'email already taken.'})
        MyUser.objects.filter(email=request.user.email).update(email=email)
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
    return redirect('landing')
