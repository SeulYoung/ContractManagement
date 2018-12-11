from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
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


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username=username)
        if not filter_result:
            raise forms.ValidationError("用户名不存在")
        return username


class UsernameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username=username)
        if len(filter_result) > 0:
            raise forms.ValidationError("用户名已存在")
        return username


class PasswordForm(forms.Form):
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
