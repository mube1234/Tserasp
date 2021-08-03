from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='login'),
    path('home/', views.index, name='index'),
    #pdf generation naol
   # path('pdf/', views.render_pdf_view, name='pdf'),   
    #path('Pdf/', views.Requestpdf.as_view(), name='pdf'),   
    path('Pdf/<pk>/', views.request_pdf, name='request-pdf'),   


    # account related
    path('register/', views.create_account, name='register'),
    path('profile/', views.profile, name='profile'),
    path('account/manage', views.account_management, name='account'),
    path('account/delete/<int:id>', views.delete_account, name='delete-account'),
    path('account-detail/<str:username>', views.account_detail, name='detail-account'),
    path('logout/', views.user_logout, name='logout'),

    # request related
    path('request/tshoview', views.tsho_view_request, name="tsho-view-request"),
    path('request/tshoapproved', views.tsho_view_approved_request, name="tsho-view-approved-request"),
    path('request/departmentview', views.department_view_request, name="department-view-request"),
    path('request/departmentdapproved', views.department_view_approved_request, name="department-view-approved-request"),
    path('request/departmentapprove/<int:id>', views.department_approve_request, name="department-approve-request"),
    path('request/tshoapproved/detail/<str:id>', views.tsho_view_approved_request_detail, name="view-detail"),
    # path('request/tapprove/<int:id>',views.tsho_assign_request,name="assign-approve-request"),
    # path('request/tapprove/<int:id>',views.send_email,name="assign-approve-request"),
    path('request/schoolview', views.school_view_request, name="school-view-request"),
    path('request/schoolapproved', views.school_view_approved_request, name="school-view-approved-request"),
    path('request/schoolapprove/<int:id>', views.school_approve_request, name="school-approve-request"),
    path('request/my_request', views.my_request, name="my-request"),
    path('request/my_request/detail/<str:id>', views.my_request_detail, name="detail-request"),
    path('request/make', views.make_request, name="make-request"),
    path('request/tshoapprove/<str:id>', views.tsho_approve_request, name="tsho-approve-request"),

    # vehicle  related
    path('vehicle/', views.vehicle_management, name="vehicle-manage"),
    path('vehicle/add', views.vehicle_register, name="vehicle-register"),
    path('vehicle/edit/<int:id>/', views.edit_vehicle, name="edit-vehicle"),
    path('vehicle/delete/<int:id>', views.delete_vehicle, name='delete-vehicle'),

    # schedule related
    path('schedule/add', views.create_schedule, name="create-schedule"),
    path('schedule/update/<str:id>', views.update_schedule, name="update-schedule"),

    # material related
    path('material/', views.material_management, name="material-manage"),
    path('addMaterial/', views.AddMaterial, name='AddMaterial'),
    path('material/', views.material_management, name="material-manage"),
    path('updatematerial/<str:pk>/', views.Updatematerial, name="Updatematerial"),
    path('deletematerial/<str:pk>/', views.deletematerial, name="delete_material"),

    # history

     path('history/', views.history, name="history"),
]
