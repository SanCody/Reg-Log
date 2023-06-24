from django.shortcuts import render, redirect
from .forms import Register, Login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
def register(req):
    form = Register(req.POST)
    if req.method=="POST":
        
        if form.is_valid():
            form.save()
            print("ok1")
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password1')

            user = authenticate(request=req, username=username, password=password)

            auth_login(req, user)
            
            return redirect('profile')
            
    return render(req, 'register.html', {'form': form})

def login(req):
    if req.method == 'POST':
        form = Login(request=req, data=req.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=req, username = username, password = password)
            
            if user is not None:
                auth_login(req, user)
                return redirect('profile')
            
    else:
        form = Login()
        
    return render(req, "login.html", {'form':form})

@login_required(login_url='login')
@never_cache
def profile(req):
    user = req.user
    return render(req, "profile.html", {'user': user})

@login_required(login_url='login')
@never_cache
def logout(req):
    auth_logout(req)
    return redirect("login")