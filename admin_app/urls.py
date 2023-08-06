from django.urls import path
from .views import *
urlpatterns = [
    path("",home_page,name = "home_page"),
    path("details/<ordre_id>",details_view,name = "details_view"),
    path("search_result/<search>",search_result,name = "search_result"),
    path("delete_ordre/<id_ordre>",delete_ordre,name = "delete_ordre"),
    path("add_ordre/",add_ordre, name = "add_ordre"),
    path("edit_ordre/<ordre_id>",edit_ordre,name = "edit_ordre"),
    path("add_image/<ordre_id>",add_image,name = "add_image"),
    path("imgs/<ordre_id>", images,name = "images"),
    path("delete_pic/<img_id>",delete_pic,name = "delete_pic"),
    path("profile/", profile_view , name = "profile_view"),
    path("edit_profile/<profile_id>",edit_profile,name = "edit_profile"),
    path("create_account/<str:type>",create_accout,name = "create_account"),
    path("create_comercial/<info>", create_commercial,name = "create_commercial"),
    path("create_tech/<info>",create_tech,name = "create_tech"),
    path("see_users/<type>", users_view, name = "users_view"),
    path("search_methods/",search_methods,name = "search_methods"),
    path("search_form/<method>",search_form,name = "search_form"),
    path("search_method_result/<result>",search_method_result,name = "search_method_result"),
    path("generate_pdf/<ordre_id>",generate_pdf, name = "generate_pdf"),
    path("add_remarque/<ordre_id>", add_remarque,name = "add_remarque" ),
    path("see_remarque/<ordre_id>",see_remarque,name = "see_remarque"),
    path("add_sav/<ordre_id>",add_sav,name = "add_sav"),
    path("generate_sav/<ordre_id>",generate_sav,name = "generate_sav")
    
]
