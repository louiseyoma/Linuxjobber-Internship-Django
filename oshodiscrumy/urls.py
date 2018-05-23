from django.urls import path

from . import views


app_name = 'oshodiscrumy'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:user_id/', views.error_page, name = 'error_page'),
    path('add_user/', views.add_user.as_view(), name = 'add_user'),
    path('move_task/', views.move_task, name = 'move_task'),
    path('add_task/', views.add_task, name = 'add_task'),
]









#urlpatterns = [
#     path('', views.IndexView.as_view(), name = 'index'),
#     path('test/', views.test, name = "test"),
#     path('users/', views.users, name = 'users'),
#     path('login/', views.login, name = 'login'),
#     path('move_task/<int:task_id>/', views.move_task, name = 'move_task'),
#     path('add_user/', views.add_user, name = 'add_user'),
#     path('add_task/', views.add_task, name = 'add_task'),
#     path('view_goal/', views.goals_view.as_view(), name = 'view_goals'),
#     # path('<int:goal_id>/changestatus/', views.change_task_status, name = 'change_task_status'),
# ]