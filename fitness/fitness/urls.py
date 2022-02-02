"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls',namespace='social')),
    path('accounts/',include('allauth.urls')),
    path('',views.index,name='index'),
    path('gender/',views.Gender.as_view(),name="gender"),
    path('hard-workout/', views.hard, name="hard-workout"),
    path('medium-workout/', views.medium, name="medium-workout"),
    path('easy-workout/', views.easy, name="easy-workout"),
    path('activity/',views.activity,name='activity'),
    path('BMI/', views.BMI, name="BMI"),
    path('be_fit/',include('be_fit.urls')),
    path('food_options', views.food_options, name='food_options'),
    path('home',views.home,name='home'),

]
