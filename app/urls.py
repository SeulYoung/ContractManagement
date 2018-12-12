from django.urls import path
from . import views
from django.conf.urls import url
from . import DataManagement
from . import ContractManagement

app_name='app'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login.html', views.login, name='login'),
    path('registration.html', views.registration, name='registration'),
    path('logout', views.logout, name='logout'),
    path('profile.html', views.profile, name='profile'),
    path('emailUpdate.html', views.email_update, name='email_update'),
    path('DraftingContract.html', views.password_update, name='password_update'),
    path('SignContract.html', views.password_update, name='password_update'),
    path('FinalContract.html', views.password_update, name='password_update'),
    path('ApprovalContract.html', views.password_update, name='password_update'),
    path('SigningContract.html', views.password_update, name='password_update'),
    url(r'^customer_add/$', DataManagement.customer_add.as_view(), name='customer_add'),
    url(r'^customer_modify/$', DataManagement.customer_modify.as_view(), name='customer_modify'),
    url(r'^customer_select/$', DataManagement.customer_select.as_view(), name='customer_select'),
    url(r'^customer_delete/$', DataManagement.customer_delete.as_view(), name='customer_delete'),
    ######################合同查询####################
    path('contract_select',ContractManagement.C_Select,name="contract_select"),
]
