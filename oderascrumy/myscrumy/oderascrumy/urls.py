"""myscrumy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

"""from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url 
from oderascrumy import views"""
from django.urls import path
from oderascrumy import views
from django.contrib.auth import views as auth_views
from .views import ScrumyUserList

app_name='oderascrumy'
urlpatterns = [
    path('', views.home, name='home'),
    path('goal/<pk>/', views.goals, name='goals'),
    path('task/<pk>/', views.move_goals, name='move_goals'),
    path('users/' , views.add_user, name= 'add_user'),
    path('userlist/', ScrumyUserList.as_view()),
]
