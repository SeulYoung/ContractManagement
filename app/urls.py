from django.urls import path
from django.conf.urls import url
from . import views
from . import DataManagement

from . import ContractManagement

app_name = 'app'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login.html', views.login, name='login'),
    path('registration.html', views.registration, name='registration'),
    path('logout', views.logout, name='logout'),
    path('profile.html', views.profile, name='profile'),
    path('UsernameUpdate.html', views.username_update, name='username_update'),
    path('PasswordUpdate.html', views.password_update, name='password_update'),

    path('DraftingContract.html', ContractManagement.drafting_contract, name='drafting_contract'),
    path('ListContract.html', ContractManagement.list_contract, name='list_contract'),
    path('SignContract.html', ContractManagement.sign_contract, name='sign_contract'),
    path('FinalContract.html', ContractManagement.final_contract, name='final_contract'),
    path('ApprovalContract.html', ContractManagement.approval_contract, name='approval_contract'),
    path('SigningContract.html', ContractManagement.signing_contract, name='signing_contract'),

    url(r'^customer_add/$', DataManagement.customer_add.as_view(), name='customer_add'),
    url(r'^customer_modify/$', DataManagement.customer_modify.as_view(), name='customer_modify'),
    url(r'^customer_select/$', DataManagement.customer_select.as_view(), name='customer_select'),
    url(r'^customer_delete/$', DataManagement.customer_delete.as_view(), name='customer_delete'),
    ######################合同查询####################
    path('contract_select', ContractManagement.C_Select, name="contract_select"),
]
