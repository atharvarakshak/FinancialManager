from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm
app_name = 'core'

urlpatterns=[
    path('',views.index,name='index'),

     path('getResponse', views.getResponse,name='getResponse'),
     path('signup',views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),

     path('contact',views.contact,name='contact'),

]
