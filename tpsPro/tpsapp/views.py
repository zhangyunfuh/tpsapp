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
def generate_password(passwd):
    sha = hashlib.sha256()
    sha.update(passwd.encode('utf-8'))
    return sha.hexdigest()

def register(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        user=User()
        user.name=request.POST.get('name')
        print(request.POST)
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
        password=generate_password(request.POST.get('password'))
        #print(request.POST)
        users=User.objects.filter(name=name).filter(password=password)
        if users.count():
            user=users.first()
            response = redirect('tpsapp:homepage')
            request.session['token']=user.token
            request.session.set_expiry(30)
            return response
        else:
            err='用户名或密码错误'
            return render(request,'login.html',{'err':err})

def logout(request):
    response=redirect('tpsapp:homepage')
    request.session.flush()
    return response


def detailed(request):
    return render(request,'detailed.html')


def cart(request):
    return render(request,'cart.html')