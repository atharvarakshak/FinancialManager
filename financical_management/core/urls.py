from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core'

urlpatterns=[
    path('',views.index,name='index'),
    #  path('chatbot', include('chatbot.urls')),
     path('getResponse', views.getResponse,name='getResponse'),

]
