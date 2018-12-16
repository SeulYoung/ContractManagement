from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
import datetime


@csrf_exempt
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

        file = request.FILES.get('files')
        print(file)
        print(file.name)

        my_contract = Contract.objects.create(name=name,
                                              customer=customer,
                                              beginTime=beginTime,
                                              endTime=endTime,
                                              content=content,
                                              userName=userName)
        my_state = State.objects.create(conNum=my_contract.num, type=1, time=nowTime)

        if file is not None:
            my_attachment = Attachment.objects.create(conNum=my_contract.num,
                                                      fileName=file.name,
                                                      uploadTime=nowTime,
                                                      file=file)
        print(my_contract)
        print(my_state)
        print(my_contract.beginTime)
        return render(request, 'DraftingContract.html')


def list_contract(request):
    contract_list = []
    process_list = Process.objects.filter(state=0, userName=request.user.username)
    for process in process_list:
        if process.type == 1:
            p_type = '会签'
        elif process.type == 2:
            p_type = '审批'
        else:
            p_type = '签订'
        contract = Contract.objects.filter(num=process.conNum).first()
        contract_list.append([process.conNum, contract.name, process.time, p_type])
    return render(request, 'ListContract.html', {'contract_list': contract_list})


def list_drafts(request):
    contract_list = Contract.objects.filter(userName=request.user.username)
    for contract in contract_list:
        state = State.objects.filter(conNum=contract.num)
        if state.type == 2:
            contract_list.append(contract)
    return render(request, 'ListContract.html', {'contract_list': contract_list})


def contract_info(request):
    if request.method == "POST":
        num = request.POST.get('num')
        p_type = request.POST.get('type')
        contract = Contract.objects.filter(num=num).first()
        if p_type == '会签':
            return render(request, 'SigningContract.html', {'contract': contract})
        elif p_type == '定稿':
            return render(request, 'FinalContract.html', {'contract': contract})
        elif p_type == '会签':
            return render(request, 'ApprovalContract.html', {'contract': contract})
        else:
            return render(request, 'SignContract.html', {'contract': contract})


def signing_contract(request):
    if request.method == "POST":
        num = request.POST.get('num')
        opinion = request.POST.get('opinion')
        Process.objects.filter(conNum=num, type=1, userName=request.user.username).update(state=1,
                                                                                          content=opinion,
                                                                                          time=datetime.datetime.now())
        filter_result = Process.objects.filter(conNum=num, type=1, state=0)
        if not filter_result:
            State.objects.create(conName=num, type=2, time=datetime.datetime.now())
        return redirect('/ListContract.html')


def final_contract(request):
    if request.method == "POST":
        pass
    return render(request, 'FinalContract.html')


def approval_contract(request):
    if request.method == "POST":
        pass
    return render(request, 'ApprovalContract.html')


def sign_contract(request):
    if request.method == "POST":
        pass
    return render(request, 'SignContract.html')


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
