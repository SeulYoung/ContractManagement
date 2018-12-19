from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
import django.utils.timezone as timezone

DatsList1=[{'name'}]
DatsList2=[{'name'}]
DatsList3=[{'name'}]


def wcon_sel(request):
    if request.method == "post":
        num = request.POST.get('conNum')
        return render(request, 'contract_assign.html', {'con_num': num})

    con_list = State.objects.filter(type=1)
    return render(request, 'Wcontract_sel.html', {'wcon_list': con_list})


def con_assign(request):

    if request.method == "POST":
        countersignP = request.POST.get('wsign_field')
        approvalP = request.POST.get('approval_field')
        signP = request.POST.get('sign_field')

        contract_list = Contract.objects.all()
        for user in contract_list:
            if user.name == name:
                con_id = user.num

        Process.objects.create(conNum=con_id, type=1, state=0, userName=countersignP)
        Process.objects.create(conNum=con_id, type=2, state=0, userName=approvalP)
        Process.objects.create(conNum=con_id, type=3, state=0, userName=signP)
    else:
        pending_list = Right.objects.all()
        role_list = Role.objects.all()

        for user in pending_list:
            for user2 in role_list:
                if user.userName==user2.name:
                    if user2.functions.find("会签合同") == -1:
                        DatsList1.__add__(user2.name)
                    if user2.functions.find("审批合同") == -1:
                        DatsList2.append(user2.name)
                    if user2.functions.find("签订合同") == -1:
                        DatsList3.append(user2.name)
    return render(request, 'Wcontract_sel.html', {'list1': DatsList1},{'list2': DatsList2},{'list3': DatsList3})


    return render(request, 'contract_assign.html.html')


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

