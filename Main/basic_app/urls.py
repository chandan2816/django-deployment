from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from basic_app import views


app_name="basic_app"

urlpatterns=[
    url('register/',views.register,name="register"),
    url('',views.index,name="index"),
    url('logout/',views.user_logout,name="user_logout"),
    url('user_login/',views.user_login,name="user_login"),
    path('admin/', admin.site.urls)




]