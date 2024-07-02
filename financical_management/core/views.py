from django.shortcuts import render,redirect
from django.http import HttpResponse


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot('chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train =[
    "hi",
    "hi there",
    "Whats your name?",
    "I'm just a chatbot",
    "Give me some finance tips",
    "What is your monthly income?",
    "I earn 1000 dollars per month",

]

ListTrainer(bot).train(list_to_train)
# Create your views here.

def index(request):

    return render(request,'core/index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')

    chatResponse = str(bot.get_response(userMessage))


    return HttpResponse(chatResponse)