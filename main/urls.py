from django.urls import path
from .views import *
urlpatterns = [
    path("",home_page,name = "main_page"),
    path("login/",login_user,name ="login_user"),
    path("logout_user/",logout_user,name = "logoutt"),

]