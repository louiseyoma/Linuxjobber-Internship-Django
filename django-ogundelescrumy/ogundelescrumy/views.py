from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser, ScrumyGoals, GoalStatus

# Create your views here.

def index(request):
  return HttpResponse("Hello World..")


def move_goal(request, task_id):
  task =  ScrumyGoals.objects.get(pk=task_id
  )
  return HttpResponse('The task is %s' % task)


def add_user(request, username, password, role):
  new_user = ScrumyUser(username=username, password=password, role=role)
  # save in db
  new_user.save()

  # get all users
  all_users = ScrumyUser.objects.all()
  output = ', '.join([user.username for user in all_users])
  
  return HttpResponse(output)
