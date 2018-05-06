__author__ = 'FRANKCHUKY'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user', views.user),
    path('adduser', views.add_user, name='adduser'),
    path('addtask', views.add_task, name='addtask'),
    path('detail', views.detail),
    path('movetask', views.move_task, name='movetask'),
    path('edittask/<int:task_id>', views.move_task, name='edittask'),
    path('user/view/<int:user_id>', views.user_profile),

]
