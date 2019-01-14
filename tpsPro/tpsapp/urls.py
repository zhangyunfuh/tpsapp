from django.conf.urls import url
from tpsapp import views

urlpatterns=[
    url(r'^$',views.homepage,name='homepage'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^detailed/$',views.detailed,name='detailed'),
    url(r'^cart/$',views.cart,name='cart'),
]
