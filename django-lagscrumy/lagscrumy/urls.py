from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:task_id>/',views.move_task, name='move_task'),

    path('<str:scrumyuser_id>/',views.add_user, name='add_user'),

    path('<int:task_id>/',views.add_task, name ='add_task'),
]