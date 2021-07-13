from django.urls import path
from . import views
# from .views import SignUpView

urlpatterns = [
    path('',views.signin,name='login'),
    path('home/',views.index,name='index'),
    path('request/tview',views.tsho_view_request,name="tsho-view-request"),
    path('request/tapproved',views.tsho_view_approved_request,name="tsho-view-approved-request"),
    path('request/dview',views.department_view_request,name="department-view-request"),
    path('request/dapproved',views.department_view_approved_request,name="department-view-approved-request"),
    path('request/dapprove/<int:id>',views.department_approve_request,name="department-approve-request"),
    path('request/approved/detail/<str:id>',views.tsho_view_approved_request_detail,name="view-detail"),
    #path('request/tapprove/<int:id>',views.tsho_assign_request,name="assign-approve-request"),
    # path('request/tapprove/<int:id>',views.send_email,name="assign-approve-request"),
    path('request/sview',views.school_view_request,name="school-view-request"),
    path('request/sapproved',views.school_view_approved_request,name="school-view-approved-request"),
    path('request/sapprove/<int:id>',views.school_approve_request,name="school-approve-request"),
    path('request/my_request',views.my_request,name="my-request"),
    path('request/make',views.make_request,name="make-request"),
    path('request/approve/<str:id>',views.tsho_approve_request,name="tsho-approve-request"),
    path('vehicle/',views.vehicle_management,name="vehicle-manage"),
    path('vehicle/add',views.vehicle_register,name="vehicle-register"),
    path('schedule/',views.create_schedule,name="create-schedule"),
    path('material/',views.material_management,name="material-manage"),
    path('register/',views.create_account,name='register'),
    path('profile/',views.profile,name='profile'),
    path('account/',views.account_management,name='account'),
    path('logout/',views.user_logout,name='logout'),
    #####Naol
    path('addMaterial/', views.AddMaterial, name='AddMaterial'),
    path('material/', views.material_management, name="material-manage"),
    path('updatematerial/<str:pk>/', views.Updatematerial, name="Updatematerial"),
    path('deletematerial/<str:pk>/', views.deletematerial, name="delete_material"),

    # path('', SignUpView.as_view(), name='signup'),
]