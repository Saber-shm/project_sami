from django.urls import path
from .views import *
urlpatterns =[
    path("",home_page, name ="commercial_home_page"),
    path("details/<ordre_id>", details_view,name = "commercial_details_view"),
    path("cimgs/<ordre_id>",imgs,name = "commercial_imgs"),
    path("add_img/<ordre_id>",add_img,name = "commercial_add_img"),
    path("delete_img/<img_id>", delete_img,name = "commercial_delete_img"),
    path("delet_ordre/<ordre_id>", delete_ordre,name = "delete_ordre2"),
    path("edit_ordre/<ordre_id>",edit_ordre,name = "commercial_edit_ordre"),
    path("add_ordre/", add_ordre, name = "commercial_add_ordre"),
    path('search_result/<result>', search_result,name = "commercial_search_result"),
    path("search_methods/", search_methods,name = "commercial_search_methods"),
    path("search_methods_form/<method>", search_form,name = "commercial_search_form"),
    path("add_remarque/<ordre_id>", add_remarque,name = "commercial_add_remarque" ),
    path("see_remarque/<ordre_id>",see_remarque,name = "commercial_see_remarque")

]