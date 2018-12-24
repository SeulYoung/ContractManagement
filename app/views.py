from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect

from .models import *
from app.forms import *
from app.models import *


class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(Q(username=username) | Q(email=username))
        if user.check_password(password):
            return user


def judgeP(name):
    right_list = Right.objects.filter(userName=name).first()
    permission = right_list.description
    per_list = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False,
                'c1': False, 'c2': False, 'c3': False,
                'd1': False, 'd2': False, 'd3': False,
                'e1': False,
                'f1': False, 'f2': False, 'f3': False, 'f4': False}
    if permission.find('起草合同') != -1:
        per_list['a1'] = True
    if permission.find('定稿合同') != -1:
        per_list['a2'] = True
    if permission.find('查询合同') != -1:
        per_list['a3'] = True
    if permission.find('删除合同') != -1:
        per_list['a4'] = True
    if permission.find('会签合同') != -1:
        per_list['b1'] = True
    if permission.find('分配会签') != -1:
        per_list['b2'] = True
    if permission.find('查询流程') != -1:
        per_list['b3'] = True
    if permission.find('新增用户') != -1:
        per_list['c1'] = True
    if permission.find('编辑用户') != -1:
        per_list['c2'] = True
    if permission.find('查询用户') != -1:
        per_list['c3'] = True
    if permission.find('查询角色') != -1:
        per_list['d1'] = True
    if permission.find('新增角色') != -1:
        per_list['d2'] = True
    if permission.find('编辑角色') != -1:
        per_list['d3'] = True
    if permission.find('配置权限') != -1:
        per_list['e1'] = True
    if permission.find('新增客户') != -1:
        per_list['f1'] = True
    if permission.find('编辑客户') != -1:
        per_list['f2'] = True
    if permission.find('查询客户') != -1:
        per_list['f3'] = True
    if permission.find('删除客户') != -1:
        per_list['f4'] = True
    return per_list


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
        per = judgeP(user.username)
        return render(request, 'profile.html', {'user': user, 'per_list': per})
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
