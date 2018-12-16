from django.db.models import Q
from django.shortcuts import render

from .models import *
import datetime


def drafting_contract(request):
    if request.method == "GET":
        return render(request, 'DraftingContract.html')
    if request.method == "POST":

        name = request.POST.get('name')
        customer = request.POST.get('customer')
        beginTime = request.POST.get('beginTime')
        endTime = request.POST.get('endTime')
        content = request.POST.get('content')
        userName = request.user.username
        nowTime = datetime.datetime.now()
        my_contract = Contract.objects.create(name=name, customer=customer, beginTime=beginTime, endTime=endTime, content=content,
                                userName=userName)
        my_state = State.objects.create(conName=name,type=1,time=nowTime)
        print(my_contract)
        print(my_state)
        print(my_contract.beginTime)
        return render(request, 'DraftingContract.html')


def list_contract(request):
    contract_list = Contract.objects.all()
    return render(request, 'ListContract.html', {'contract_list': contract_list})


def sign_contract(request):
    return render(request, 'SignContract.html')


def final_contract(request):
    return render(request, 'FinalContract.html')


def approval_contract(request):
    return render(request, 'ApprovalContract.html')


def signing_contract(request):
    return render(request, 'SigningContract.html')


def C_Select(request):
    print(request.method)
    if request.method == "GET":
        contract_list = Contract.objects.all()
        # print(contract_list[0].beginTime)
        return render(request, 'Contract_select.html', {'contract_list': contract_list})
    if request.method == "POST":
        s_name = request.POST['name']
        contract_list = Contract.objects.filter(Q(name__icontains=s_name)).order_by('num')
        return render(request, 'Contract_select.html', {'contract_list': contract_list})
