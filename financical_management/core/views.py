from django.shortcuts import render,redirect
from django.http import HttpResponse


from chatterbot import ChatBot



# Create your views here.

def index(request):

    return render(request,'core/index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')

    return HttpResponse(userMessage)