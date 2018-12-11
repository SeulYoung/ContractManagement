import re

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView


class customer_add(TemplateView):
    template_name = "customer_add.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_add.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        address = request.POST.get('address')
        fax = request.POST.get('fax')
        tel = request.POST.get('tel')
        code = request.POST.get('code')
        bank = request.POST.get('bank')
        account = request.POST.get('account')
        remark = request.POST.get('remark')





class customer_modify(TemplateView):
    template_name = "customer_modify.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_modify.html')

class customer_select(TemplateView):
    template_name = "customer_select.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_select.html')

class customer_delete(TemplateView):
    template_name = "customer_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'customer_delete.html')

