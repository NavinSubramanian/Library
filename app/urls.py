from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('home',home,name="home"),
    path('signup',signup,name="signup"),
    path('login',login,name="login"),
    path('dashboard',dashboard,name="dashboard"),
    path('admin',admin,name="admin"),
    path('logout',logout,name="logout"),
    path('addbooks',addbooks,name="addbooks"),
    path('search',search,name="search"),
]
