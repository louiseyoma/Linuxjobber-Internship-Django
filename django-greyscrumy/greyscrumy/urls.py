from django.urls import path

from . import views

app_name = 'greyscrumy'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.Add_Task.as_view(), name='Add_Task'),
    path('<int:task_id>/', views.Move_Goal, name='Move_Goal'),
    path('add_user/', views.Add_User.as_view(), name='Add_User'),
    

]