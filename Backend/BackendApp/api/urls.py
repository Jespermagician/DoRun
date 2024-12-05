# from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.cust_login, name='login'),
    path('home',views.home,name='home'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('resetpassword',views.resetpassword,name='ResetPassword')
]