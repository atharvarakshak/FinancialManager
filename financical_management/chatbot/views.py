from django.shortcuts import render,redirect


# Create your views here.

def chatbot(request):

    return render(request,'chatbot.html')