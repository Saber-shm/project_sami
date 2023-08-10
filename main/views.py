from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import *
# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        try:
            admin_info = Administrateur.objects.get(user = request.user)

            return redirect("home_page")
        except:
            try:
                commercial_info = Comercial.objects.get(user = request.user)
                return redirect("commercial_home_page")
            except:
                try:
                    tech_info = Tech.objects.get(user = request.user)
                    return redirect("tech_home_page")
                except:
                    return redirect("login_user")
    else:
        return redirect("login_user")
def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("main_page")

    
    return render(request,"login_user.html",{}) 

def logout_user(request):
    logout(request)
    return redirect("login_user")