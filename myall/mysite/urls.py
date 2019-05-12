"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views,test
from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('',views.hoststatus,name='ini_hoststatus'),
    re_path(r'hoststatus\/$',views.hoststatus,name='hoststatus'),
    #path('hoststatus/<str:a>',views.pushmoni,name='pushmoni'),
    path('admin/', admin.site.urls),
    path('factory/', include('factory.urls')),
    path('alarms/',include('alarms.urls')),
]
