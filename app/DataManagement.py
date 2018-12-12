import re

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class customer_add(TemplateView):
    template_name = "customer_add.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_add.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        address = request.POST.get('address')
        fax = request.POST.get('fax')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        bank = request.POST.get('bank')
        account = request.POST.get('account')
        remark = request.POST.get('remark')

        customer_list = Customer.objects.all()
        print(customer_list)

        Customer.objects.create(name=name, address=address, fax=fax, tel=tel, email=email, bank=bank,
                            account=account, remark=remark)

        return HttpResponseRedirect('/customer_select')






class customer_modify(TemplateView):
    template_name = "customer_modify.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_modify.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        if tel is None:
            customer_list = Customer.objects.all()
            user_exist = False
            for user in customer_list:
                if user.name == name:
                    user_exist = True
                    return render(request, 'customer_modify.html', {'user': user})
                else:
                    continue

            return render(request, 'customer_modify.html', {'not_found': "User not found"})
        else:
            address = request.POST.get('address')
            fax = request.POST.get('fax')
            tel = request.POST.get('tel')
            email = request.POST.get('email')
            bank = request.POST.get('bank')
            account = request.POST.get('account')
            remark = request.POST.get('remark')
            Customer.objects.filter(name=name).update(tel=tel,fax=fax,email=email,address=address,bank=bank,account=account,remark=remark)

            return render(request, 'customer_modify.html', {'complish': "User modify complish"})

class customer_select(TemplateView):
    template_name = "customer_select.html"

    def get(self, request, *args, **kwargs):
        customer_list = Customer.objects.all()

        return render(request, 'customer_select.html',{'customer_list':customer_list})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        customer_list = Customer.objects.all()
        user_exist = False
        for user in customer_list:
            if user.name == name:
                user_exist = True
                return render(request, 'customer_select.html', {'user': user})
            else:
                continue

        return render(request, 'customer_select.html', {'not_found': "User not found"})


class customer_delete(TemplateView):
    template_name = "customer_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_delete.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        address =request.POST.get('address')
        print(name, tel, address)
        if tel is None:
            customer_list = Customer.objects.all()
            user_exist = False
            for user in customer_list:
                if user.name == name:
                    user_exist = True
                    return render(request, 'customer_delete.html', {'user': user})
                else:
                    continue

            return render(request, 'customer_delete.html', {'not_found': "User not found"})
        else:

            Customer.objects.filter(name=name).delete()

            return render(request, 'customer_delete.html', {'complish': "User delete complish"})