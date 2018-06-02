from django.urls import path
from eyomascrumy import views

app_name = 'eyomascrumy'

urlpatterns = [
	path('eyomascrumy',views.homepage, name = 'homepage'),
]