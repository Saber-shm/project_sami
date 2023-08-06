from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page,name = "tech_home_page"),
    path("details/<ordre_id>", details_view,name = "tech_details_view"),
    path("imgs/<ordre_id>", imgs,name = "tech_imgs"),
    path("add_img/<ordre_id>", add_img,name = "tech_add_img"),
    path("delete_img/<img_id>",delete_img,name ="tech_delete_img"),
    path("search_method/", search_methods, name = "tech_search_method"),
    path("search_form/<method>", search_form,name = "tech_search_form"),
    path("search_result/<result>",search_method_result,name = "tech_search_method_result"),
    path("add_remarque/<ordre_id>", add_remarque,name = "tech_add_remarque" ),
    path("see_remarque/<ordre_id>",see_remarque,name = "tech_see_remarque"),
    path("add_sav/<ordre_id>",add_sav,name = "tech_add_sav")
]