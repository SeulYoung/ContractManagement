from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
import django.utils.timezone as timezone


def wcon_sel(request):
    out_list = []
    if request.method == "POST":
        s_con = request.POST.get('s_con')
        if s_con:
            c_list = Contract.objects.filter(name=s_con).first()
            if c_list:
                con_list = State.objects.filter(conNum=c_list.num).first()
                isexist = Process.objects.filter(conNum=c_list.num)
                if not isexist:
                    out_list.append({'conName': s_con, 'time': con_list.time})
        else:
            state_list = State.objects.filter(type=1)
            for user in state_list:
                c_list = Contract.objects.filter(num=user.conNum).first()
                isexist = Process.objects.filter(conNum=user.conNum)
                if not isexist:
                    out_list.append({'conName': c_list.name, 'time': user.time})
        return render(request, 'Wcontract_sel.html', {'wcon_list': out_list})

    state_list = State.objects.filter(type=1)
    for user in state_list:
        c_list = Contract.objects.filter(num=user.conNum).first()
        isexist = Process.objects.filter(conNum=user.conNum)
        if not isexist:
            out_list.append({'conName': c_list.name, 'time': user.time})

    return render(request, 'Wcontract_sel.html', {'wcon_list': out_list})


def con_assign(request):
    if request.method == "POST":
        con_name = request.POST.get('conName')
        num_list = Contract.objects.filter(name=con_name).first()

        countersignp = request.POST.getlist('check_box_list1')
        approvalp = request.POST.getlist('check_box_list2')
        signp = request.POST.getlist('check_box_list3')
        if not countersignp or not approvalp or not signp:
            role_list1 = Right.objects.filter(description__contains='会签合同')
            role_list2 = Right.objects.filter(description__contains='审批合同')
            role_list3 = Right.objects.filter(description__contains='签订合同')
            return render(request, 'contract_assign.html',{'role_list1': role_list1,'role_list2': role_list2,
                                                           'role_list3': role_list3, 'conName': con_name})
        else:
            Process.objects.create(conNum=num_list.num, type=1, state=0, userName=countersignp, time=timezone.now())
            Process.objects.create(conNum=num_list.num, type=2, state=0, userName=approvalp, time=timezone.now())
            Process.objects.create(conNum=num_list.num, type=3, state=0, userName=signp, time=timezone.now())
            return HttpResponseRedirect('Wcontract_sel.html')


def wper_sel(request):
    out_list = []
    if request.method == "POST":
        s_name = request.POST.get('s_name')
        if s_name:
            user_list = User.objects.filter(username=s_name).first()
            if not user_list:
                return render(request, 'Wpermission_sel.html', {'msg': '所查找的用户不存在'})
            else:
                right_list = Right.objects.filter(userName=user_list.username).first()
                if right_list:
                    out_list.append({'username': user_list.username, 'rolename': right_list.roleName})
                else:
                    out_list.append({'username': user_list.username, 'rolename': '无'})
                return render(request, 'Wpermission_sel.html', {'out_list': out_list})

    user_list = User.objects.all()
    for user in user_list:
        right_list = Right.objects.filter(userName=user.username).first()
        if right_list:
            out_list.append({'username': user.username, 'rolename': right_list.roleName})
        else:
            out_list.append({'username': user.username, 'rolename': '无'})
    return render(request, 'Wpermission_sel.html', {'out_list': out_list})


def permission_assign(request):
    if request.method == "POST":
        u_name=request.POST.get('user_w')
        permission = request.POST.get('check_box_list')
        if permission:
            role_msg = Role.objects.filter(name = permission).first()
            Right.objects.create(userName = u_name, roleName = permission, description = role_msg.functions)
            return HttpResponseRedirect('Wpermission_sel.html')
        else:
            right_list = Right.objects.filter(userName=u_name).first()
            if right_list:
                return HttpResponseRedirect('Wpermission_sel.html')
            role_list = Role.objects.all()
            return render(request, 'permission_assign.html', {'user_w': u_name, 'role_list': role_list})


def role_sel(request):
    if request.method == "POST":
        name = request.POST.get('s_name')
        d_name = request.POST.get('d_name')
        if name:
            role_list = Role.objects.filter(name=name)
            if not role_list:
                return render(request, 'role_sel.html', {'d_msg': '未找到要查询的角色'})
            return render(request, 'role_sel.html', {'role_list': role_list})
        else:
            if d_name:
                Role.objects.filter(name=d_name).delete()
                role_list = Role.objects.all()
                return render(request, 'role_sel.html', {'role_list': role_list, 'd_msg': '删除成功'})
            role_list = Role.objects.all()
            return render(request, 'role_sel.html', {'role_list': role_list})

    else:
        role_list = Role.objects.all()
        return render(request, 'role_sel.html', {'role_list': role_list})


def role_add(request):

    if request.method == "POST":
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')
        permission = request.POST.getlist('check_box_list')
        if not role_name:
            return render(request, 'role_add.html', {'r_error': '未输入角色名称'})
        else:
            role_list = Role.objects.all()
            for user in role_list:
                if user.name == role_name:
                    return render(request, 'role_add.html', {'r_error': '该角色已存在，请重新输入'})

            Role.objects.create(name = role_name, description = description, functions = permission)
            return HttpResponseRedirect("role_sel.html")

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
    if request.method == 'POST':
        role_name = request.POST.get('m_name')
        description = request.POST.get('description')
        permission = request.POST.getlist('check_box_list')
        if not description:
            role_list = Role.objects.all()
            return render(request, 'role_mod.html', {'m_name': role_name, 'role_list': role_list, 'mod':"mod"})
        else:
            Role.objects.filter(name=role_name).update(description=description, functions=permission)
            return HttpResponseRedirect("role_sel.html")

    role_list = Role.objects.all()
    return render(request, 'role_mod.html', {'role_list': role_list})


def user_sel(request):
    return render(request, 'user_sel.html')


def user_add(request):
    return render(request, 'user_add.html')


def user_mod(request):
    return render(request, 'user_mod.html')


def user_del(request):
    return render(request, 'user_sel.html')

