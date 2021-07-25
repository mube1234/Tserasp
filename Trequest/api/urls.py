from django.urls import path
from Trequest.api import views

urlpatterns = [
    path('view/', views.schedule_list),
    path('view/detail/<str:pk>/',views.schedule_detail)

]