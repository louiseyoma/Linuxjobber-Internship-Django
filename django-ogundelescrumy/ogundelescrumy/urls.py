from django.urls import path

from . import views

urlpatterns = [
  path('', views.index),
  path('tasks/<int:task_id>/', views.move_goal, name='move_goal'),
  path('user/<str:username>/<str:password>/<str:role>/', views.add_user, name='add_user'),
  ]