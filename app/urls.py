from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url

from ContractManagement import settings
from . import views
from . import DataManagement
from . import ContractManagement
from . import SystemManagement

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
                  path('ListDraft.html', ContractManagement.list_draft, name='list_draft'),
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
                  url(r'^contract_select/$', ContractManagement.C_Select, name="contract_select_null"),
                  url(r'^contract_select/(?P<pagenum>\d+)/$', ContractManagement.C_Select, name="contract_select"),
                  url(r'^contract_process/$', ContractManagement.C_Process, name="contract_process_null"),
                  url(r'^contract_process/(?P<state>\d+)/$', ContractManagement.C_Process, name="contract_process"),

                  path('Wcontract_sel.html', SystemManagement.wcon_sel, name='Wcon_sel'),
                  path('Wpermission_sel.html', SystemManagement.wper_sel, name='Wper_sel'),
                  path('contract_assign.html', SystemManagement.con_assign, name='con_assign'),
                  path('permission_assign.html', SystemManagement.permission_assign, name='permission_assign'),
                  path('role_add.html', SystemManagement.role_add, name='role_add'),
                  path('role_mod.html', SystemManagement.role_mod, name='role_mod'),
                  path('role_sel.html', SystemManagement.role_sel, name='role_sel'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
