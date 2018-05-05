from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Goal, User, Status
from .forms import AddUser, AddTask, MoveTask


def index(request):
    try:
        username = User.objects.all()
        #for user in username:
       #     allUser.append(user.goal_set.filter(status__status__iexact='WG'))
    except User.DoesNotExist:
        raise Http404("Does not exist")
    context = {'username': username}
    return render(request, "odekhiranscrumy/index.html", context)

def move_goal(request, task_id):
    goal = Goal.objects.get(id=task_id)
    #user.goal.set.all()
    return HttpResponse(goal)


def add_user(request):
    user = User.objects.all()
    AddUserForm = AddUser(request.POST)
    context = {'form': AddUserForm, 'user': user}

    if AddUserForm.is_valid():
        AddUserForm.save()
    return render(request, "odekhiranscrumy/add_user.html", context)


def add_task(request):
    AddTaskForm = AddTask(request.POST)
    new_task = {'form': AddTaskForm}

    if AddTaskForm.is_valid():
        AddTaskForm.save()
    return render(request, "odekhiranscrumy/add_task.html", new_task)
