from django.urls import path

from . import views

app_name = 'greyscrumy'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:task_id>/', views.Move_Goal, name='Move_Goal'),
    path('add_user/', views.Add_User.as_view(), name='Add_User'),

]