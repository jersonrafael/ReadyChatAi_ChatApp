from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import *

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

from . import models



def getMessages():
    url = 'https://www.dev.readychatai.com/messages_json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Create your views here.
@login_required(login_url=" /chat/login/ ")
def chat_home_view(request):
    user = request.user
    all_messages = getMessages()
    local_messages = models.message.objects.all()
    if all_messages != None:
        context = {'messages':all_messages, 'user':user, 'local_messages':local_messages}
        return render(request, template_name='chat/index.html', context=context)
    else:
        return render(request, template_name='404.html')

@login_required(login_url="/chat/login/")
def chat_message_view(request,id):
    user = request.user
    all_messages= getMessages()
    local_messages = models.message.objects.all()
    context ={
        'message':all_messages,
        'user':user,
        'local_messages':local_messages
    }
    if all_messages != None:
        print("Si hay m")
        for message in all_messages:
            if message["id"] == id:
                context = {
                    'messages':all_messages,
                    'message':message,
                    'local_messages':local_messages
                    }
                return render(request,template_name='chat/message.html', context=context)
    else:
        return render(request, template_name='404.html')


@login_required(login_url="/chat/login/")
def chat_my_message_view(request,pk):
    user = request.user
    all_messages= getMessages()
    local_messages = models.message.objects.all()
    local_message = models.message.objects.get(id=pk)
    context ={
        'messages':all_messages,
        'local_messages':local_messages,
        'local_message':local_message,
        'user':user,
    }
    if all_messages != None:
        return render(request,template_name='chat/my_message.html', context=context)
    else:
        return render(request, template_name='404.html')

@login_required(login_url="/chat/login/")
def send_message_view(request):
    user = request.user
    all_messages= getMessages()
    local_messages = models.message.objects.all()
    form = message_form(request.POST)
    context = {
        'messages':all_messages,
        'form':form,
        'user':user,
        'local_messages':local_messages

    }

    if request.method == 'POST':
        if form.is_valid():
            print("Soy valido")
            model = models.message.objects.create(owner=user,to=form.cleaned_data.get("to"),text=form.cleaned_data.get("text"))
            model.save()
            return redirect('/chat/messages/')

    if all_messages != None:
        return render(request, template_name='chat/new_message.html', context=context)
    else:
        return render(request, template_name='404.html')

def chat_login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request,user)
                return redirect("/chat/messages/")
            else:
                form = LoginForm(request.POST)
                message = 'Check the credentials'
                return render(request, template_name='chat/login.html', context={'message':message, 'form':form})                
        else:
            message = 'an error has occurred'
            return render(request, template_name='chat/login.html', context={'message':message})

    return render(request, template_name='chat/login.html',context={'form':form})

def chat_singup_view(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect('/chat/messages/')
        else:
            message = 'an error has occurred'
            return render(request, template_name='chat/create_account.html', context={'message':message, 'form':form})

    return render(request, template_name='chat/create_account.html', context={'form':form})

def chat_logout_view(request):
    logout(request)
    return redirect("/chat/login/")