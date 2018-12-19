from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
import django.utils.timezone as timezone


def wcon_sel(request):
    con_list = State.objects.filter(type=1)
    return render(request, 'Wcontract_sel.html', {'wcon_list': con_list})


def con_assign(request):
    if request.method == "POST":
        num = request.POST.get('conNum')
        countersignp = request.POST.getlist('check_box_list1')
        if not countersignp:
            role_list1 = Right.objects.filter(description__contains='会签合同')
            role_list2 = Right.objects.filter(description__contains='审批合同')
            role_list3 = Right.objects.filter(description__contains='签订合同')
            return render(request, 'contract_assign.html',{'role_list1': role_list1,'role_list2': role_list2,
                                                           'role_list3': role_list3, 'con_num':num})

        else:
            approvalp = request.POST.getlist('check_box_list2')
            signp = request.POST.getlist('check_box_list3')

            Process.objects.create(conNum=num, type=1, state=0, userName=countersignp, time=timezone.now())
            Process.objects.create(conNum=num, type=2, state=0, userName=approvalp, time=timezone.now())
            Process.objects.create(conNum=num, type=3, state=0, userName=signp, time=timezone.now())

    con_list = State.objects.filter(type=1)
    return render(request, 'Wcontract_sel.html', {'wcon_list': con_list})


def wper_sel(request):
    right_list = Right.objects.all()
    user_list = User.objects.all()
    return render(request, 'Wpermission_sel.html', {'right_list': right_list, 'user_list': user_list})


def permission_assign(request):
    if request.method == "POST":
        u_name=request.POST.get('user_w')
        permission = request.POST.get('check_box_list')
        if permission:
            role_msg = Role.objects.filter(name = permission).first()
            Right.objects.create(userName = u_name, roleName = permission, description = role_msg.functions)

            right_list = Right.objects.all()
            user_list = User.objects.all()
            return render(request, 'Wpermission_sel.html', {'right_list': right_list, 'user_list': user_list})
        else:
            role_list = Role.objects.all()
            return render(request, 'permission_assign.html', {'user_w': u_name, 'role_list': role_list})


def role_sel(request):
    if request.method == "POST":
        name = request.POST.get('s_name')
        if name:
            role_list = Role.objects.all()
            for user in role_list:
                if user.name == name:
                    return render(request, 'role_sel.html', {'user': user})
                else:
                    continue
        else:
            d_name = request.POST.get('d_name')
            Role.objects.filter(name=d_name).delete()
            return render(request, 'role_sel.html', {'d_msg': '删除成功'})
    else:
        role_list = Role.objects.all()
        return render(request, 'role_sel.html', {'role_list': role_list})


def role_add(request):

    if request.method == "POST":
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')
        permission = request.POST.getlist('check_box_list')
        if role_name is None:
            return render(request, 'role_add.html', {'r_error': '未输入角色名称'})
        else:
            role_list = Role.objects.all()
            for user in role_list:
                if user.name == role_name:
                    return render(request, 'role_add.html', {'r_error': '该角色已存在，请重新输入'})

            Role.objects.create(name = role_name, description = description, functions = permission)

            role_list = Role.objects.all()
            return render(request, 'role_sel.html', {'role_list': role_list})

    return render(request, 'role_add.html')


def role_del(request):
    delr_name = request.POST.get('delR_name')
    role_list = Role.objects.all()
    right_list = Right.objects.all()
    ise = False
    for user in role_list:
        if user.name == delr_name:
            ise = True
            Role.objects.filter(name = delr_name).delete()

    for user in right_list:
        if user.roleName == delr_name:
            ise = True
            Right.objects.filter(roleName = delr_name).delete()

    if ise:
        return render(request, 'role_sel.html',{'isn_exist': '该角色不存在，请重新输入'})
    else:
        return render(request, 'role_sel.html')


def role_mod(request):

    return render(request, 'role_mod.html')

