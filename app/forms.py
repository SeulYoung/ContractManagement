from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise forms.ValidationError("用户名最短6个字符")
        elif len(username) > 50:
            raise forms.ValidationError("用户名最长50个字符")
        else:
            filter_result = User.objects.filter(username=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("用户名已存在")
        return username

    def clean_email(self):
        try:
            email = self.cleaned_data.get('email')
        except ValidationError:
            raise forms.ValidationError("邮箱格式错误")
        filter_result = User.objects.filter(email=email)
        if len(filter_result) > 0:
            raise forms.ValidationError("邮箱已被注册")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 4:
            raise forms.ValidationError("密码最短4个字符")
        elif len(password1) > 20:
            raise forms.ValidationError("密码最长20个字符")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次密码不一致")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(Q(username=username) | Q(email=username))
        if not filter_result:
            raise forms.ValidationError("用户名不存在")
        return username


class EmailForm(forms.Form):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        try:
            email = self.cleaned_data.get('email')
        except ValidationError:
            raise forms.ValidationError("邮箱格式错误")
        filter_result = User.objects.filter(email=email)
        if len(filter_result) > 0:
            raise forms.ValidationError("邮箱已被注册")
        return email


class PasswordForm(forms.Form):
    old_password = forms.CharField(label='OldPassword', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError("密码最短6个字符")
        elif len(password1) > 20:
            raise forms.ValidationError("密码最长20个字符")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次密码不一致")
        return password2
