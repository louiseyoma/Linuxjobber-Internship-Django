from django.urls import path
from eyomascrumy import views

app_name = 'eyomascrumy'

urlpatterns = [
	path('eyomascrumy',views.homepage, name = 'homepage'),
	#path('eyomascrumy/<str:usersView>/', views.addTask, name = 'detail'),
	path('eyomascrumy/<str:username>/', views.findUser, name = 'users'),
	path('eyomascrumy/user/new', views.addUser, name = 'addUser'),
]