from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView, DetailView
from adesokanscrumy import views
from .models import ScrumyGoals



# Create your views here.

urlpatterns = [
path('index', views.index, name='index'),
#path('index', ListView.as_view(queryset=ScrumyGoals.objects.all())),
path('index2',views.home, name= 'home'),
path('movegoal/<int:task_id>', views.move_goal),
path('adduser/', views.add_user)
]


