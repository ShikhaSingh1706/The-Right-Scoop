# authentication/views.py
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register_page(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        #basic validation
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect("register-page")
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("register-page")
        
        #create user(Save to database)
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Registration successful. please login.")
        
  

    return render(request, 'authentication/register.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)#creates session
            messages.success(request,"Login Successful")
            # return redirect("dashboard")

        else:
            messages.error(request,"Invalid username or password")  
            return redirect("login-page")  
    return render(request, 'authentication/login.html')
