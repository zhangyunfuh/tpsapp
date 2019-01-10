from django.conf.urls import url
from tpsapp import views

urlpatterns=[
    url(r'^$',views.homepage,name='homepage'),
    url(r'^sign/$',views.sign,name='sign')
]
