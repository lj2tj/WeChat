from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'server'

urlpatterns = [
    path('', views.wechat_home, name='default'),
    path(r'index/', views.index, name='index'),
]