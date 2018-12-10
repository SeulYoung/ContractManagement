from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login.html', views.login, name='login'),
    path('registration.html', views.registration, name='registration'),
    path('logout', views.logout, name='logout'),
    path('profile.html', views.profile, name='profile'),
    path('emailUpdate.html', views.email_update, name='email_update'),
    path('passwordUpdate.html', views.password_update, name='password_update'),
    url(r'^customer_add/$', views.customer_add.as_view(), name='customer_add'),
    url(r'^customer_modify/$', views.customer_modify.as_view(), name='customer_modify'),
    url(r'^customer_select/$', views.customer_select.as_view(), name='customer_select'),
    url(r'^customer_delete/$', views.customer_delete.as_view(), name='customer_delete'),
]
