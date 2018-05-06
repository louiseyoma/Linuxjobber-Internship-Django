from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib import messages
from .models import ScrumyGoals,GoalStatus,ScrumyUser
from .forms import ChangeTaskStatusForm,UserForm
from django.views.generic import TemplateView, View
from django.views import generic

def index(request):
    users = ScrumyUser.objects.all()
    context = {'users':users}
    return render(request, 'okoroscrumy/index.html', context)

def get_users(request):
    users = ScrumyUser.objects.all()
    context = {'users':users}
    return render(request, 'okoroscrumy/users.html', context)

class add_user(TemplateView):

    def get(self, request):
        form = UserForm()
        goals = ScrumyUser.objects.all()
        return render(request, 'okoroscrumy/adduser.html', {'form':form, 'goals': goals })

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():

            success = 'Registered Successfully'
            form.save()

            name = form.cleaned_data['fullname']
            role = form.cleaned_data['role']

            form = UserForm()
        goals = ScrumyUser.objects.all()

        args = {'form': form, 'name': name, 'role': role, 'goals': goals, 'success': success}

        return render(request, 'okoroscrumy/adduser.html', args)

def dailytask_goals(request):
    status_dt= GoalStatus.objects.get(status='DT')
    goals = status_dt.scrumygoals_set.all()
    context = {'goals':goals}
    return render(request, 'okoroscrumy/dailytask.html', context)

def move_goal(request, task_id):
    try:
        goals = ScrumyGoals.objects.get(task_id=task_id)
    except ScrumyGoals.DoesNotExist:
        raise Http404('No goal with this task_id' + str(task_id))
    context = {'goals':goals, 'task_id':task_id}
    return render(request, 'okoroscrumy/goals.html', context)

class add_task(generic.ListView):
    template_name = 'okoroscrumy/addtask.html'
    
    def get_queryset(self):
        return ScrumyGoals.objects.all()

def ChangeTaskStatus(request, goal_id):
    if request.method == "POST":
        form = ChangeTaskStatusForm(request.POST)
        if form.is_valid:
            NewStatus = request.POST.get('status_id')
            status = GoalStatus.objects.get(id=NewStatus)
            try:
                goal = ScrumyGoals.objects.get(id=goal_id)
            except ScrumyGoals.DoesNotExist:
                raise Http404('No goal with this id' + str(goal_id))
            goal.status_id = status
            goal.save()
            return redirect('okoroscrumy:index')
    else:
        form = ChangeTaskStatusForm()
        context = {'form':form}
        return render(request, 'okoroscrumy/changestatus.html', context)
