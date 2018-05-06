from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('move_task/<int:task_id>/', views.move_task, name='move_task' ),
    path('add_task/', views.add_task, name='add_task'),
    path('add_user/', views.add_user, name='add_user'),
    #path('register/', views.register, name = 'register'),
]
