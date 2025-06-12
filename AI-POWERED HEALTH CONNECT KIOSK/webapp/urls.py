"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. adddata the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('doctor/', views.doctor, name="doctor"),
    path('doctorsignup/', views.doctorsignup, name="doctorsignup"),
    path('dsignupaction/', views.dsignupaction, name="dsignupaction"),

    
    
    
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    path('dloginaction/', views.dloginaction, name="dloginaction"),
    
    
    path('userhome/', views.userhomedef, name="userhomedef"),
    path('userlogout/', views.userlogoutdef, name="userlogoutdef"),
    
    path('dhome/', views.dhomedef, name="dhomedef"),
    path('dlogout/', views.dlogoutdef, name="dlogoutdef"),
    
    path('adminlogout/', views.adminlogout, name="userlogoutdef"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('upload/', views.upload, name="upload"),
    path('upload1/', views.upload1, name="upload1"),
    path('adddata/', views.adddata, name="adddata"),
    
    path('viewdoc/', views.viewdoc, name="viewdoc"),
    path('addquery/', views.addquery, name="addquery"),


    path('training/', views.training, name="training"),
    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('nntrain/', views.nntrain, name="nntrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('testing/', views.testing, name="testing"),
    path('viewacc/', views.viewacc, name="viewacc"),

    path('chatdoctor/', views.chatdoctor, name="chatdoctor"),
    path('dchatpage/', views.dchatpage, name="dchatpage"),
    path('dchat/', views.dchat, name="dchat"),
    path('dchataction/', views.dchataction, name="dchataction"),

    path('pchatpage/', views.pchatpage, name="pchatpage"),
    path('pchat/', views.pchat, name="pchat"),
    path('pchataction/', views.pchataction, name="pchataction"),
    path('chatpage2/', views.chatpage2, name="chatpage2"),
    path('getmesg/', views.getmesg, name="getmesg"),
    

    
    

    
    




    path('chatpage/', views.chatpage, name="chatpage"),
    path('chataction/', views.chataction, name="chataction"),

    path('option/<str:op>/', views.option, name="option"),
    path('index.html', views.home, name="index"),

]
