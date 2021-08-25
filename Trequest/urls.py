from django.urls import path, re_path
# for password reset
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.signin, name='login'),
    path('home/', views.index, name='index'),
    # re_path(r'/', views.notifications, name='notify'),
    # pdf generation naol
    # path('pdf/', views.render_pdf_view, name='pdf'),
    #path('Pdf/', views.Requestpdf.as_view(), name='pdf'),
    path('Pdf/<pk>/', views.request_pdf, name='request-pdf'),


    # account related
    path('register/', views.create_account, name='register'),
    path('profile/', views.profile, name='profile'),
    path('account/manage', views.account_management, name='account'),
    path('account/delete/<int:id>', views.delete_account, name='delete-account'),
    path('account/edit/', views.edit_account, name='edit-account'),
    path('edit/user/<int:id>', views.edit_user_account, name='edit-user-account'),
    path('account-detail/<str:username>',views.account_detail, name='detail-account'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change-password'),
    path('ajax/load_department', views.load_department,name='ajax_load_department'),

    # vehicle request related
    path('request/tshoview', views.tsho_view_request, name="tsho-view-request"),
    path('request/tshoapproved', views.tsho_view_approved_request, name="tsho-view-approved-request"),
    path('request/departmentview', views.department_view_request, name="department-view-request"),
    path('request/departmentdapproved', views.department_view_approved_request, name="department-view-approved-request"),
    path('request/departmentapprove/<int:id>', views.department_approve_request, name="department-approve-request"),
    path('request/tshoapproved/detail/<str:id>', views.tsho_view_approved_request_detail, name="view-detail"),
    path('request/schoolview', views.school_view_request, name="school-view-request"),
    path('request/schoolapproved', views.school_view_approved_request, name="school-view-approved-request"),
   
    path('request/schoolapprove/<int:id>', views.school_approve_request, name="school-approve-request"),
    path('request/tshoapproved', views.tsho_view_approved_request,name="tsho-view-approved-request"),
    path('request/departmentview', views.department_view_request,name="department-view-request"),
    path('request/departmentdapproved', views.department_view_approved_request,name="department-view-approved-request"),
    path('request/departmentapprove/<int:id>',views.department_approve_request, name="department-approve-request"),
    path('request/tshoapproved/detail/<str:id>',views.tsho_view_approved_request_detail, name="view-detail"),
    path('request/schoolview', views.school_view_request,name="school-view-request"),
    path('request/schoolapproved', views.school_view_approved_request,name="school-view-approved-request"),
    path('request/schoolapprove/<int:id>',views.school_approve_request, name="school-approve-request"),
    path('request/my_request', views.my_request, name="my-request"),
    path('request/my_request/detail/<str:id>',views.my_request_detail, name="detail-request"),
    path('request/make', views.make_request, name="make-request"),
    path('request/cancel/<int:id>', views.cancel_request, name="cancel-request"),
    path('request/reject/<int:id>',views.reject_request,name="reject-request"),
    path('request/tshoapprove/<str:id>', views.tsho_approve_request, name="tsho-approve-request"),
    path('vehicle/repaired',views.repaired_vehicle,name='repaired-vehicle'),
#     path('vehicle/vehicle_type_register',views.vehicle_type_register,name='vehicle-type-register'),
    path('request/tshoapprove/<str:id>',
         views.tsho_approve_request, name="tsho-approve-request"),
    path('vehicle/repaired', views.repaired_vehicle, name='repaired-vehicle'),

    
    
    # vehicle  related
    path('vehicle/', views.vehicle_management, name="vehicle-manage"),
    path('vehicle/add', views.vehicle_register, name="vehicle-register"),
    path('vehicle/edit/<int:id>/', views.edit_vehicle, name="edit-vehicle"),
    path('vehicle/delete/<int:id>', views.delete_vehicle, name='delete-vehicle'),
    path('vehicle/assigned/',views.assigned_request,name='assigned-request'),

    # schedule related
    path('schedule/add', views.create_schedule, name="create-schedule"),
    path('schedule/update/<str:id>', views.update_schedule, name="update-schedule"),
   
    # report
    path('report/', views.annual_report, name="report"),
    # Activity Log
    path('activitylog/', views.ActivityLogs, name="log"),

    #  password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="Trequest/password_reset_form.html"), name='password-reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="Trequest/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Trequest/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="Trequest/password_reset_complete.html"), name='password_reset_complete'),
    # Driver Evaluation
    path('evaluate/', views.evaluate, name="evaluate-driver"),


    # feedback
    path('feedback/create_feedback', views.feedback, name="create-feedback"),
    path('feedback/view_feedback', views.view_feedback, name="view-feedback"),

]
