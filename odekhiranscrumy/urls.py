from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('move_goal/<task_id>/', views.move_goal, name='move'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/', views.add_task, name='add_tasks'),

]