from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'owolabiscrumy'
urlpatterns = [
	path('', views.index, name='index'),
	url(r'^adduser$', views.add_user, name = 'add_user'),
	path('<int:task_id>/', views.move_task, name='move_task'),
	path('add_task/', views.add_task, name='add_task'),
	path('details/', views.details, name="details")

]
