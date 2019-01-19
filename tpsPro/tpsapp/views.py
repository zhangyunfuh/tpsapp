import hashlib
import random
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from tpsapp.alipay import alipay
from tpsapp.models import User, wheel, Detail, Cart

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
    carts = Cart.objects.all()
    return render(request,'homepage.html',{'name':name,'comps':comp,'imgs':imgs,'carts':carts})

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
    carts=Cart.objects.all()
    return render(request, 'detailed.html', {'name': name,'detail':detail,'carts':carts})



def cart(request):
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    if users.count():
        user = users.first()
        name = user.name
    else:
        name = None
    carts=Cart.objects.all()
    idten=random.randrange(10000,10000000)
    return render(request,'cart.html',{'name':name,'carts':carts,'idtens':idten})


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

    print(token)
    if token:
        users=User.objects.get(token=token)
        detailid=request.GET.get('detailid')
        details=Detail.objects.get(id=detailid)
        carts=Cart.objects.filter(user=users).filter(products=details)
        if carts.exists():
            cart=carts.first()
            cart.number=request.GET.get('numb')
            cart.save()
            msg={'msg':'{}-修改购物车成功'.format(details.title),'number':cart.number,'status':1}
            return JsonResponse(msg)
        else:
            carts = Cart()
            carts.user = users
            carts.products = details
            carts.number=request.GET.get('numb')
            carts.isselect=True
            carts.save()
            msg={'msg':'{}-添加购物车成功'.format(details.title),'number':carts.number,'status':1}
            return JsonResponse(msg)
    else:

        return JsonResponse({'msg':'登入后购买','status':0})


def appnotify(request):
    return JsonResponse({'msg':'success'})


def returnview(request):
    return redirect('tpsapp:homepage')


def pay(request):
    ident=request.GET.get('ident')
    totals=request.GET.get('total')
    alipayurl=alipay.direct_pay(
        subject='book-2018',
        out_trade_no=ident,
        total_amount=totals,
        return_url='http://47.106.251.205/returnview/'

    )
    alipayurl='https://openapi.alipaydev.com/gateway.do?{data}'.format(data=alipayurl)
    return  JsonResponse({'alipayurl':alipayurl,'status':1})
  