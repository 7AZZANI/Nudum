from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name= "main"),
    path('services', views.developtment_services, name= "service"),
    path('software-development', views.soft_development, name= "softdev"),
]



