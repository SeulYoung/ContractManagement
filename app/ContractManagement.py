from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import *


def drafting_contract(request):
    return render(request, 'DraftingContract.html')


def sign_contract(request):
    return render(request, 'SignContract.html')


def final_contract(request):
    return render(request, 'FinalContract.html')


def approval_contract(request):
    return render(request, 'ApprovalContract.html')


def signing_contract(request):
    return render(request, 'SigningContract.html')


def C_Select(request):
    return render(request, 'Contract_select.html')
