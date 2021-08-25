from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('addmaterial/', views.AddMaterial, name='AddMaterial'),
    path('material/', views.material_management, name="material-manage"),
    
    path('updatematerial/<str:pk>/', views.Updatematerial, name="Updatematerial"),
    path('deletematerial/<str:pk>/', views.deletematerial, name="delete_material"),
    path('deleterequest/<str:pk>/', views.delete_request, name="delete_request"),

    path('materialrequest/', views.material_request, name="material-request"),
    path('materialdetail/<str:id>/', views.material_detail, name="material_detail"),
    path('materialrequest/',views.material_request, name="material-request"),
    path('view_material_request/', views.view_material_request, name="view_material_request"),
    path('view_request/', views.view_request, name="view_request"),
    path('alert/', views.view_alert, name="alert"),



]