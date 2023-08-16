from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('sname')
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        Cpassword = request.POST.get('cpwd')

        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name= first_name,last_name=last_name, username=username,password=password)
                user.save()
                messages.info(request, "Registered")
                return redirect('login')  # Redirect to login page
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    return render(request,'registration.html')

def login(request):
     if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
     else:
         return render(request,'login.html')

def logoutt(request):
    logout(request)
    return redirect('index')
