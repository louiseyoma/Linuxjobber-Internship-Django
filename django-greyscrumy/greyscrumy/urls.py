from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name = 'greyscrumy'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'greyscrumy/login.html'}),
    # path('register/', views.RegisterFormView.as_view(), name='register'),
    path('add_task/', views.Add_Task.as_view(), name='Add_Task'),
    path('<int:task_id>/', views.Move_Task, name='Move_Task'),
    path('add_user/', views.Add_User.as_view(), name='Add_User'),
    
]