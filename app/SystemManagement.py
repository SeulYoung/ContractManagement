from django.shortcuts import render
from .models import *

DatsList1=[{'name'}]
DatsList2=[{'name'}]
DatsList3=[{'name'}]

def Wcon_sel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        con_list = State.objects.all()
        for user in con_list:
            if user.name == name:
                return render(request, 'Wcontract_sel.html', {'wcon_list': user})
            else:
                continue
    else:
        con_list = State.objects.filter(type=1)
        return render(request, 'Wcontract_sel.html', {'wcon_list': con_list})


def con_assign(request, name):
    if request.method == "POST":
        countersignP = request.POST.get('wsign_field')
        approvalP = request.POST.get('approval_field')
        signP = request.POST.get('sign_field')

        contract_list = Contract.objects.all()
        for user in contract_list:
            if user.name == name:
                con_id = user.num

        Process.objects.create_user(conNum=con_id, type=1, state=0, userName=countersignP)
        Process.objects.create_user(conNum=con_id, type=2, state=0, userName=approvalP)
        Process.objects.create_user(conNum=con_id, type=3, state=0, userName=signP)
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


def permission_assign(request):
    return render(request, 'contract_assign.html')


def role_sel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        role_list = Role.objects.all()
        for user in role_list:
            if user.name == name:
                return render(request, 'role_sel.html', {'user': user})
            else:
                continue
    else:
        role_list = Role.objects.all()
        return render(request, 'role_sel.html', {'role_list': role_list})


def role_add(request):

    if request.method == "POST":
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')
        permission = request.POST.getlist('right')
        if role_name is None:
            return render(request, 'role_add.html', {'unfilled': '未输入角色名称'})
        else:
            role_list = Role.objects.all()
            for user in role_list:
                if user.name == role_name:
                    return render(request, 'role_add.html', {'is_exist': '该角色已存在，请重新输入'})

            Role.objects.create(name = role_name, description = description)
            Right.objects.create(roleName=role_name,description=permission)

            return render(request, 'role_sel.html', {'user': user})
    return render(request, 'contract_assign.html')


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
    return render(request, 'contract_assign.html')

