from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from .models import Pizza

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "Orders/login.html")
    
    return render(request, "Orders/index.html")    

def dashboard(request):
    username=request.POST["username"]
    password=request.POST["password"]
    print("......................")
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print(user)
    if (user is not None):
        print("]]]]]]]]]]]]]]")
        login(request, user)
        print('????????????')
        print(username)
        print(password)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "Orders/signup.html") 

    

def logout_view(request):
    logout(request)
    return render(request, "Orders/login.html")  


def signup(request):
    username=request.POST["username"]
    password=request.POST["password"]

    user = User.objects.create_user(username, username, password)
    user.save()
    print("**********8")
    print(user.email)
    user = authenticate(request, username=user.email, password=user.password)
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print(user)
    if (user is not None):
        print("]]]]]]]]]]]]]]")
        login(request, user)
        print('????????????')
        print(username)
        print(password)
        return HttpResponseRedirect(reverse("index"))

    return HttpResponse("ok")