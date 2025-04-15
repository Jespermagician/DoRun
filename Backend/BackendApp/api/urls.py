# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),         # Register an new user
    path('login/', views.cust_login, name='login'),             # login an user 
    path('home',views.home,name='home'),                        # user page
    path('adminhome',views.adminhome,name='adminhome'),         # adminpage
    path('UpdateDonations',views.UpdateDonations,name='UpdatDonations'),   
    path('UpdateUsers',views.UpdateUsers,name='UpdateUsers'),
    path('resetpassword',views.resetpassword,name='ResetPassword'),
    path('reset-user-pwd',views.resetUserPasswort,name='ResetUserPasswort'),
    path('DelDonoRec',views.DelDonoRec,name='DelDonoRec'),
    path('DelUser',views.DelUser,name='DelUser'),
    path('csrf-token/',views.csrf_token_view),
    path('get-users', views.get_users, name='get-users'), # get all details
    path('set-km', views.set_km, name='set-km'), # get all details
    path('generate-pwd', views.generate_pwd, name='generate-pwd'), # get all details
]