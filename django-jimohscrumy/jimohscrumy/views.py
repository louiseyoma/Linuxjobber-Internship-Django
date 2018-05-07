from django.shortcuts import render
from django.template import loader
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from jimohscrumy.models import ScrumyGoal, ScrumyUser, GoalStatus
from jimohscrumy.forms import GoalForm, UserForm


def index(request):
    try:
        users = ScrumyUser.objects.all()
        for user in users:
            goal = ScrumyGoal.objects.filter(Goal_type='W')

    except ScrumyUser.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, "myscrumy/index.html", {'users': users})


def move_goal(request, task_id):
    mygoals = ScrumyGoal.objects.get(pk=task_id)
    return HttpResponse(mygoals)


def add_user(request):
    AddUserForm = UserForm(request.POST)
    context = {'form': AddUserForm}
    if AddUserForm.is_valid():
        AddUserForm.save()

    return render(request, "myscrumy/add_user.html", context)


def add_task(request):
    if request.method == 'POST':
        AddTaskForm = GoalForm(request.POST)
        if AddTaskForm.is_valid():
            AddTaskForm.save()
            return redirect('')
    else:
        AddTaskForm = GoalForm()
        return render(request, 'myscrumy/add_task.html', {'form': AddTaskForm})


def goal(request):
    goals = ScrumyGoal.objects.filter(Goal_type='D')
    output = ','.join([u.title for u in goals])
    return HttpResponse(goals)


def detail(request, user_id):
    try:
        goal = ScrumyGoal.objects.filter(Goal_type='W')
        user = ScrumyUser.objects.get(pk=user_id)

    except ScrumyUser.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, 'myscrumy/detail.html', {'user': user})
