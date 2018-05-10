from . import views 
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^move/(?P<task_id>\d+)/$', views.move_task, name = 'move_goal'),
     url(r'^adduser$', views.add_user, name = 'add_user'),
     url(r'^addtask$', views.add_task, name = 'add_task'),
     url('view_goal/', views.goals_view.as_view(), name='view_goals')
   ]
