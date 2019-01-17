import hashlib
import random
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from tpsapp.models import User, wheel,  Detail

from django.http import HttpResponse,HttpRequest
def homepage(request):
    token=request.session.get('token')
    users=User.objects.filter(token=token)
    if users.count():
        user=users.first()
        name=user.name
    else:
        name=None
    comp=Detail.objects.all()
    imgs=wheel.objects.all()
    return render(request,'homepage.html',{'name':name,'comps':comp,'imgs':imgs})

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
        user.token = generate_token()
        user.save()
        response=redirect('tpsapp:homepage')

        request.session['token']=user.token
        request.session.set_expiry(0)
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
            request.session.set_expiry(0)
            return response
        else:
            err='用户名或密码错误'
            return render(request,'login.html',{'err':err})

def logout(request):
    response=redirect('tpsapp:homepage')
    request.session.flush()
    return response


def detailed(request,proid):
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    if users.count():
        user = users.first()
        name = user.name
    else:
        name = None
    detail=Detail.objects.get(id=proid)
    return render(request, 'detailed.html', {'name': name,'detail':detail})



def cart(request):
    return render(request,'cart.html')


def checkuser(request):
    username=request.GET.get('username')
    users=User.objects.filter(name=username)
    if users.exists():
        return JsonResponse({'msg': '账号被占用','status':0})
    else:
        return JsonResponse({'msg': '可以使用！','status':1})

#
# def detailed2(request):
#     token = request.session.get('token')
#     users = User.objects.filter(token=token)
#     if users.count():
#         user = users.first()
#         name = user.name
#     else:
#         name = None
#     return render(request, 'detailed2.html', {'name': name})

def addcart(request):
    token=request.session.get('token')
    print('添加购物车')
    if token:
        pass
    else:
        return JsonResponse({'msg':'登入后操作','status':0})