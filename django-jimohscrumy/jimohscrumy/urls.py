from django.urls import path
from django.contrib.auth.views import login
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'myscrumy/login.html'}),
    path('jimohscrumy/', views.index, name='index'),
    path('goal/<int:task_id>/', views.move_goal, name="move_goal"),
    path('add_user/', views.add_user, name="add_user"),
    path('add_task/', views.add_task, name="add_task"),
    #path('<user_id>/', views.detail, name="user_detail"),
]
