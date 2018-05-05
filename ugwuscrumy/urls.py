from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.move_goal, name='move_goal'),
    path('addtask/<int:task_id>/', views.add_task, name='add_task'),
    path('adduser',views.add_user)
]
