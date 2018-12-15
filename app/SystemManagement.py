from django.shortcuts import render
from .models import *


def Wcon_sel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        con_list = State.objects.all()
        for user in con_list:
            if user.name == name:
                return render(request, 'customer_select.html', {'user': user})
            else:
                continue
    else:
        con_list = State.objects.all()

        return render(request, 'Wcontract_sel.html', {'con_list': con_list})


def con_assign(request, name):
    if request.method == "POST":
        countersignP = request.POST.get('sign_field')
        approvalP = request.POST.get('approval_field')
        signP = request.POST.get('sign_field')

        contract_list = Contract.objects.all()
        for user in contract_list:
            if user.name == name:
                con_id = user.num

        Process.objects.create_user(conNum=con_id, type=1, state=0, userName=countersignP)
        Process.objects.create_user(conNum=con_id, type=2, state=0, userName=approvalP)
        Process.objects.create_user(conNum=con_id, type=3, state=0, userName=signP)

    return render(request, 'Wcontract_sel.html')


def permission_assign(request):
    return render(request, 'contract_assign.html')


def role_add(request):
    return render(request, 'contract_assign.html')


def role_del(request):
    return render(request, 'contract_assign.html')


def role_mod(request):
    return render(request, 'contract_assign.html')


def role_sel(request):
    return render(request, 'contract_assign.html')
