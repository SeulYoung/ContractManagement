import re

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def drafting_contract(request):
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
        print(contract_list[0].content)
        return render(request, 'Contract_select.html',{'contract_list':contract_list})
    if request.method == "POST":
        s_name = request.POST['name']
        contract_list = Contract.objects.filter(Q(name__icontains=s_name)).order_by('num')
        return render(request, 'Contract_select.html',{'contract_list':contract_list})