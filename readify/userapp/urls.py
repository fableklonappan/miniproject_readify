from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logoutt/',views.logoutt,name='logoutt')
]