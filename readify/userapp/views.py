from django.shortcuts import render, redirect
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, redirect

from django.contrib import messages, auth
from .models import CustomUser
# from accounts.backends import EmailBackend
from django.contrib.auth import get_user_model


User = get_user_model()


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        if email and password:
            user = authenticate(request, email=email, password=password)
            print("Authenticated user:", user)  # Print the user for debugging
            if user is not None:
                auth_login(request, user)
                print("User authenticated:", user.email, user.role)
                return redirect('http://127.0.0.1:8000/')
            else:
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Please fill out all fields."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('sname')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        role = User.CUSTOMER
        # print(first_name,last_name,password,role)
        if first_name and last_name and email  and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'login.html', {'error_message': error_message})

            else:

                user = User(first_name=first_name, last_name=last_name, email=email, role=role)
                user.set_password(password)
                user.save()
                return render(request,'login.html')

    return render(request, 'registration.html')


# def vhowner(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('sname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role = User.SELLER
#         print(first_name,last_name,password,role)
#         if first_name and last_name and email and role and password:
#             if User.objects.filter(email=email).exists():
#                 error_message = "Email is already registered."
#                 return render(request, 'login.html', {'error_message': error_message})

#             else:

#                 user = User(first_name=first_name, last_name=last_name, email=email, role=role)
#                 user.set_password(password)
#                 user.save()
#                 return render(request,'login.html')

#     return render(request, 'registration.html')



def logout(request):
    auth.logout(request)
    return redirect('index')


def profile(request):
    return render(request, "profile.html")

    #           error_message = "Email is already registered."
    #           return render(request,"register.html",{'error_message': error_message})
    #           error_message = ''