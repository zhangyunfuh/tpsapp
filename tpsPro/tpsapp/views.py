import hashlib
import random
import time
from django.shortcuts import render, redirect

# Create your views here.
from tpsapp.models import User

from django.http import HttpResponse,HttpRequest
def homepage(request):
    token=request.session.get('token')
    users=User.objects.filter(token=token)
    if users.count():
        user=users.first()
        name=user.name
    else:
        name=None
    return render(request,'homepage.html',{'name':name})

def generate_token():
    token =str(time.time()) + str(random.random())
    md5=hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()
def generate_password(password):
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

def register(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        user=User()
        user.name=request.POST.get('name')
        user.password=generate_password(request.POST.get('password'))

        user.token=generate_token()
        user.save()
        response=redirect('tpsapp:homepage')
        request.session['token']=user.token
        return response
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        #print(request.POST)
        users=User.objects.filter(name=name)
        if users.count():

            user=users.first()
            user.token=generate_token()
            user.save()
            request.session['token']=user.token
            request.session.set_expiry(30)
            response = redirect('tpsapp:homepage')
            return response
        else:
            return render(request,'login.html',{'err':'用户名或密码错误'})

def logout(request):
    response=redirect('tpsapp:homepage')
    request.session.flush()
    return response
