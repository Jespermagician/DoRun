# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.cust_login, name='login'),
    path('home',views.home,name='home'),
    path("hello/", views.index, name="index"),   
    #path('success/', views.success, name='success'),    # Erfolgsseite
]