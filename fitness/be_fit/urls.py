from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path("signup",views.signup,name = 'signup'),
    path("login",views.login,name='login'),
    path("logout",auth_views.LogoutView.as_view(),name='logout'),
    path("forgot_pass",views.forgot_pass,name='forgot_pass'),
    # path("otp/", views.otp, name='otp'),
    path("otp/<int:user>/", views.otp, name='otp'),
    path("set_new_pass/<int:id>/",views.set_new_pass,name='set_new_pass'),
    path('wrongattempts', views.wrongattempts, name='wrongattempts'),

]