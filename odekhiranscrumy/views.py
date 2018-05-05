from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Goal, User, GoalStatus
from .forms import NewUserForm


def index(request):
    username = []
    totalUser = User.objects.count()
    return totalUser
    try:
        for user in range(1, totalUser):
            username.append(User.objects.get(pk=user))
            return username
        context = {'username': username}
        return render(request, "odekhiranscrumy/index.html", context)
    except User.DoesNotExist:
        raise Http404("Does not exist")

def move_goal(request, task_id):
    goal = Goal.objects.get(id=task_id)
    #user.goal.set.all()
    return HttpResponse(goal)


def add_user(request):
    user = User.objects.all()
    newUserForm = NewUserForm(request.POST)
    context = {'form': newUserForm, 'user': user}

    if newUserForm.is_valid():
        newUserForm.save()
    return render(request, "odekhiranscrumy/add_user.html", context)
