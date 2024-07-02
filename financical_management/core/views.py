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
    "How much do you save?",
    "I save 100 dollars per month",
    "What is your monthly expenses?",
    "I spend 900 dollars per month",
    "How much do you invest?",
    "I invest 100 dollars per month",
    "What is your monthly savings rate?",
    "I save 10% of my monthly income",
    "What is your monthly investment rate?",
    "I invest 10% of my monthly income",
    "What is your monthly expense rate?",
    "I spend 90% of my monthly income",
    "What is your monthly saving rate?",
    "I save 10% of my monthly income",
    "What is your monthly investment rate?",
    "I invest 10% of my monthly income",
    "What is your monthly expense rate?",
    "I spend 90% of my monthly income",
    "How much do you spend on food per month?",
    "I spend 300 dollars per month on food",
    "How much do you spend on rent per month?",
    "I spend 400 dollars per month on rent",
    "How much do you spend on transportation per month?",
    "I spend 100 dollars per month on transportation",
    "How much do you spend on entertainment per month?",
    "I spend 100 dollars per month on entertainment",
    "How much do you spend on utilities per month?",
    "I spend 100 dollars per month on utilities",
    

]

ListTrainer(bot).train(list_to_train)
# Create your views here.

def index(request):

    return render(request,'core/index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')

    chatResponse = str(bot.get_response(userMessage))


    return HttpResponse(chatResponse)