from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import *
from admin_app.forms import *
from .forms import *



def home_page(request):
    if request.user.is_authenticated:
        commercial_info = Comercial.objects.get(user = request.user)
        data = Order.objects.all()
        data = reversed(data)
        if request.method == "POST":
            search = request.POST["search"]
            return redirect("commercial_search_result", result = search)
        return render(request,'commercial_home.html',{"data":data})
    else:
        return redirect("login_user")

def search_result(request,result):
    if request.user.is_authenticated:
        commercial_info = Comercial.objects.get(user = request.user)
        data = Order.objects.filter(nom__contains = result)
        return render(request,"commercial_search_result.html",{"data":data})
    else:
        return redirect("login_user")
def details_view(request,ordre_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)

        ordre_data = Order.objects.get(pk = ordre_id)
        return render(request,'commercial_details_view.html',{"data":ordre_data})
    else:
        return redirect("login_user")

def add_ordre(request):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        if request.method == "POST":
            form = add_ordre_form(request.POST)
            if form.is_valid():
                ordre = form.save(commit=False)
                ordre.posted_by = request.user
                ordre.save()
                return redirect("commercial_home_page")
        else:
            form = add_ordre_form

        return render(request,"commercial_add_ordre.html",{"form":form})
    else:
        return redirect("login_user")
def imgs(request,ordre_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        ordre = Order.objects.get(pk = ordre_id)
        data = Image.objects.filter(ordre = ordre_id)
        return render(request,"commercial_imgs.html",{'data': data})
    else:
        return redirect("login_user")
def delete_ordre(request,ordre_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        ordre = Order.objects.get(pk = ordre_id)
        ordre.delete()
        return redirect("commercial_home_page")
    else:
        return redirect("login_user")
    
def delete_img(request,img_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        img = Image.objects.get(pk = img_id)
        ordre_id = img.ordre.id
        img.delete()
        return redirect("commercial_imgs",ordre_id = ordre_id)
    else:
        return redirect("login_user")

def add_img(request,ordre_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_image_form(request.POST,request.FILES)
            if form.is_valid():
                img = form.save(commit=False)
                img.ordre = ordre
                img.posted_by = request.user
                img.save()
                return redirect("commercial_details_view",ordre_id = ordre_id)

        else:
            form = add_image_form
        return render(request,"commercial_add_img.html",{"form":form})
    else:
        return redirect("login_user")
def edit_ordre(request,ordre_id):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        ordre_data = Order.objects.get(pk = ordre_id)
        form = add_ordre_form(request.POST or None, instance=ordre_data)
        if form.is_valid():
            form.save()
            return redirect("commercial_details_view",ordre_id)
        return render(request,"edit_ordre.html",{"form": form})
    else:
        return redirect("login_user")
def add_sav(request,ordre_id):
    if request.user.is_authenticated:
        
        
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_sav_form(request.POST)
            if form.is_valid():
                sav = form.save(commit = False)
                sav.posted_by = request.user
                sav.ordre = ordre
                sav.save()
                return redirect("detail_view", ordre_id = ordre_id)
        else:
            form = add_sav_form
        return render(request,'add_sav_form.html',{"form":form})
    else:
        return redirect("login_user")
def search_methods(request):
    if request.user.is_authenticated:
        return render(request,"commercial_search_methods.html",{})

    else:
        return redirect(request,"login_user")
def search_form(request,method):
    if request.user.is_authenticated:
        commercial_user_info = Comercial.objects.get(user = request.user)
        if request.method == "POST":
            search = request.POST["search"]
            if method == "email":
                data_email = f"{search}|{method}"
                return redirect("commercial_search_result",result = data_email)
            elif method == "nom":
                data_nom = f"{search}|{method}"
                return redirect("commercial_search_result",result = data_nom)
            elif method =="pn":
                data_pn = f"{search}|{method}"
                return redirect("commercial_search_result", result = data_pn)
        return render(request,"commercial_search_form.html",{"method" : method})
    else:
        return redirect("login_user")
def search_method_result(request,result):
    if request.user.is_authenticated:
        result = result.split('|')
        print(result)
        method = result[-1]
        if method == "email":
            data = Order.objects.filter(email__contains = result[0])
        elif method == "pn":
            data = Order.objects.filter(ntel = result[0])
        elif method == "nom":
            data = Order.objects.filter(nom__contains = result[0])
        return render(request,'commercial_search_result.html',{"data":data})

    else:
        return redirect("login_user")
    
def add_remarque(request,ordre_id):
    if request.user.is_authenticated:
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_remarque_form(request.POST)
            if form.is_valid():
                remarque = form.save(commit = False)
                remarque.posted_by = request.user
                remarque.ordre = ordre
                remarque.save()
                return redirect("commercial_details_view",ordre_id = ordre_id)
        else:
            form = add_remarque_form
        return render(request,'commercial_add_remarque.html',{"form": form})
    else:
        return redirect("login_user")
def see_remarque(request,ordre_id):
    if request.user.is_authenticated:
        ordre = Order.objects.get(pk = ordre_id)
        data = Remarque.objects.filter(ordre = ordre)
        return render(request,"remarque.html",{"data":data})
    else:
        return redirect("login_user")
