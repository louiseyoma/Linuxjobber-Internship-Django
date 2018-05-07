from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import json
from nwanzescrumy.models import *
from .form import *
# Create your views here.

def index(request): 
    users = []
    for obj in ScrumyUser.objects.all():
        assigned = Task.objects.filter(assigned_to=obj.id)
        obj.tasks = assigned
        users.append(obj)
    return render(request, 'index.html', {'users': users})


def user(request):
    users = ScrumyUser.objects.all().count()
    for id in range(1, users):
        try:
            user = ScrumyUser.objects.get(id=id)
        except ScrumyUser.DoesNotExist:
            raise Http404("User does not exist")
    return render(request, 'user.html', {'user': user})


def detail(request):
    status = GoalStatus.objects.get(status='weekly target')
    users = ScrumyUser.objects.all().first().scrumygoal_set.filter(status_id=status.id)
    # return json.dumps(users);
    return render(request, 'details.html', {'users': users})


def user_profile(request, user_id):
    users = ScrumyUser.objects.count()
    return render(request, 'index.html', {'users': users})


def move_goal(request, task_id):
    scrumy_goal = ScrumyGoal.objects.filter(task_id=task_id)
    return HttpResponse(scrumy_goal)


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = 1

            ScrumyUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                email=email,
                password=password,
                role_id=role
            )
            return render(request, 'adduser.html', {'form': UserForm(), 'success': True})

        return render(request, 'adduser.html', {'form': form})

    else:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})

def add_task(request):
    
    tasks = []
    for obj in Task.objects.all():
        assigned = ScrumyUser.objects.filter(id=obj.assigned_to).first()
        obj.user = assigned
        tasks.append(obj)
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']

            Task.objects.create(
                description=description,
                created_by=ScrumyUser.objects.all().first(),
                status=GoalStatus.objects.all().first(),
            )
            return render(request, 'addtask.html', {'tasks': tasks, 'form': TaskForm(), 'success': True})
        return render(request, 'addtask.html', {'tasks': tasks, 'form':form})

    else:
        form = TaskForm()
        return render(request, 'addtask.html', {'tasks': tasks, 'form': form})

def move_task(request, task_id):
    task = Task.objects.get(id=task_id)
    assigned = ScrumyUser.objects.filter(id=task.assigned_to).first()     
    if request.method == "POST":
        form = ChangeTaskStatusForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            goal = form.cleaned_data['goal']
            assigned_to = form.cleaned_data['assigned_to']

            task.description = description
            task.status_id = goal
            task.assigned_to = assigned_to
            task.save()
            return render(request, 'movetask.html', {'form': ChangeTaskStatusForm(initial={'goal': task.status.id, 'description': task.description}), 'success': True})
        return render(request, 'movetask.html', {'form':form})

    else:
        form = ChangeTaskStatusForm(initial={'goal': task.status.id, 'assigned_to': '' if assigned is None else assigned.id, 'description': task.description})
        return render(request, 'movetask.html', {'form': form})
