import datetime

from django.db import models


class Role(models.Model):
    name = models.CharField(verbose_name='name', max_length=40, primary_key=True)
    description = models.CharField(verbose_name='description', max_length=100)
    functions = models.CharField(verbose_name='functions', max_length=500)


class Right(models.Model):
    userName = models.CharField(verbose_name='userName', max_length=20, primary_key=True)
    roleName = models.CharField(verbose_name='roleName', max_length=20)
    description = models.CharField(verbose_name='description', max_length=100)


class Function(models.Model):
    num = models.CharField(verbose_name='num', max_length=10, primary_key=True)
    name = models.CharField(verbose_name='description', max_length=40)
    URL = models.CharField(verbose_name='URL', max_length=100)
    description = models.CharField(verbose_name='description', max_length=100)


class Contract(models.Model):
    num = models.CharField(verbose_name='num', max_length=20, primary_key=True)
    name = models.CharField(verbose_name='name', max_length=40)
    customer = models.CharField(verbose_name='customer', max_length=40)
    beginTime = models.DateTimeField(verbose_name='beginTime')
    endTime = models.DateTimeField(verbose_name='endTime')
    content = models.TextField(verbose_name='content')
    userName = models.CharField(verbose_name='userName', max_length=40)



class Process(models.Model):
    conNum = models.CharField(verbose_name='conNum', max_length=20, primary_key=True)
    type = models.IntegerField(verbose_name='type')
    state = models.IntegerField(verbose_name='state')
    userName = models.CharField(verbose_name='userName', max_length=40)
    content = models.TextField(verbose_name='content')
    time = models.DateField(verbose_name='time')


class State(models.Model):
    conName = models.CharField(verbose_name='conName', max_length=40, primary_key=True)
    type = models.IntegerField(verbose_name='type')
    time = models.DateField(verbose_name='time')


class Log(models.Model):
    userName = models.CharField(verbose_name='userName', max_length=40)
    content = models.TextField(verbose_name='content')
    time = models.DateField(verbose_name='time')


class Customer(models.Model):
    # num = models.BigAutoField(verbose_name='num', max_length=20, primary_key=True)
    name = models.CharField(verbose_name='name', max_length=40)
    address = models.CharField(verbose_name='address', max_length=100)
    tel = models.CharField(verbose_name='tel', max_length=20)
    fax = models.CharField(verbose_name='fax', max_length=20)
    email = models.EmailField(verbose_name='email', max_length=20)
    bank = models.CharField(verbose_name='bank', max_length=50)
    account = models.CharField(verbose_name='account', max_length=50)
    remark = models.CharField(verbose_name='remark', max_length=200)



class Attachment(models.Model):
    conNum = models.CharField(verbose_name='conNum', max_length=20, primary_key=True)
    fileName = models.CharField(verbose_name='fileName', max_length=100)
    path = models.CharField(verbose_name='path', max_length=100)
    type = models.CharField(verbose_name='type', max_length=20)
    uploadTime = models.DateField(verbose_name='uploadTime')
