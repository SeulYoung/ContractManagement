from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from app.middleware import GlobalRequestMiddleware
from app.models import *


@receiver(pre_save, sender=User, dispatch_uid="user_save_handler")
def user_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        if request is not None:
            username = request.user.username
            content = '创建用户:' + instance.username
        else:
            username = instance.username
            content = '注册用户:' + instance.username
        Log.objects.create(userName=username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=User, dispatch_uid="user_delete_handler")
def user_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '删除用户:' + instance.username
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Role, dispatch_uid="role_save_handler")
def role_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '创建角色:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=Role, dispatch_uid="role_delete_handler")
def role_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '删除角色:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Right, dispatch_uid="right_save_handler")
def right_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '为用户:' + instance.userName + ' 分配角色:' + instance.roleName
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=Right, dispatch_uid="right_delete_handler")
def right_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '收回用户:' + instance.userName + ' 的角色:' + instance.roleName
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Function, dispatch_uid="function_save_handler")
def function_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '创建功能:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=Function, dispatch_uid="function_delete_handler")
def function_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '删除功能:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Contract, dispatch_uid="contract_save_handler")
def contract_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        filter_result = Contract.objects.filter(num=instance.num)
        if len(filter_result) > 0:
            content = '定稿合同:' + instance.name
        else:
            content = '起草合同:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=Contract, dispatch_uid="contract_delete_handler")
def contract_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '删除合同:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Process, dispatch_uid="process_save_handler")
def process_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        filter_result = Contract.objects.filter(num=instance.num)
        if len(filter_result) > 0:
            if instance.type == 1:
                content = '合同:' + instance.conNum + ' 完成会签:' + instance.userName
            elif instance.type == 2:
                content = '合同:' + instance.conNum + ' 完成审批:' + instance.userName
            else:
                content = '合同:' + instance.conNum + ' 完成签订:' + instance.userName
        else:
            if instance.type == 1:
                content = '合同:' + instance.conNum + ' 分配会签:' + instance.userName
            elif instance.type == 2:
                content = '合同:' + instance.conNum + ' 分配审批:' + instance.userName
            else:
                content = '合同:' + instance.conNum + ' 分配签订:' + instance.userName
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=State, dispatch_uid="state_save_handler")
def state_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        pass


@receiver(pre_save, sender=Customer, dispatch_uid="customer_save_handler")
def customer_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '创建客户:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_delete, sender=Customer, dispatch_uid="customer_delete_handler")
def customer_delete_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '删除客户:' + instance.name
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())


@receiver(pre_save, sender=Attachment, dispatch_uid="attachment_save_handler")
def attachment_save_handler(sender, instance=None, **kwargs):
    if instance is not None:
        request = GlobalRequestMiddleware.getRequest()
        content = '上传附件:' + instance.fileName
        Log.objects.create(userName=request.user.username, content=content, time=datetime.datetime.now())
