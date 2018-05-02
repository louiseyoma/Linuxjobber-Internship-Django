from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from jimohscrumy.models import ScrumyGoal, ScrumyUser, GoalStatus


def index(request):
    goals = ScrumyGoal.objects.filter(Goal_type='D')
    output = ','.join([u.title for u in goals])
    return HttpResponse(goals)


def move_goal(request, task_id):
    mygoals = ScrumyGoal.objects.get(pk=task_id)
    return HttpResponse(mygoals)


def add_user(request, name, email, role, username, age):
    p = ScrumyUser()
    p.Name = name
    p.Email = email
    p.Age = age
    p.Role = role
    p.Username = username
    p.save()
    users = ScrumyUser.objects.all()
    output = ', '.join([eachuser.Username for eachuser in users])
    return HttpResponse(output)
