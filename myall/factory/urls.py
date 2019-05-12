from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pushdata/', views.pushdata, name='pushdata'),
    path('test/', views.test, name='test'),
    ]
