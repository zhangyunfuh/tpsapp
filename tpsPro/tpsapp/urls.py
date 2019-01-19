from django.conf.urls import url
from tpsapp import views

urlpatterns=[
    url(r'^$',views.homepage,name='homepage'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^detailed/(\d+)/$',views.detailed,name='detailed'),
    # url(r'^detailed2/$',views.detailed2,name='detailed2'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),
    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^appnotify/$',views.appnotify,name='appnotify'),
    url(r'^returnview/$',views.returnview,name='returnview'),
    url(r'^pay/$',views.pay,name='pay'),

]
