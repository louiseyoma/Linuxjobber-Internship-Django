from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import generic
from .models import ScrumyGoals, ScrumyUser, GoalStatus
from .forms import AddUserForm, AddTaskForm


class IndexView(generic.ListView):
    template_name = 'oshodiscrumy/index.html'
    context_object_name = 'goals_object'

    def get_queryset(self):
        return ScrumyUser.objects.all()


def error_page(request, user_id):
    try:
        user = ScrumyUser.objects.get(pk=user_id)
    except ScrumyUser.DoesNotExist:
        raise Http404('Page Does not exist')
    return render(request, 'oshodiscrumy/error_page.html', {'user': user})


class add_user(generic.ListView):
    def get(self, request):
        form = AddUserForm()
        goals = ScrumyUser.objects.all()
        return render(request, 'oshodiscrumy/add_user.html', {'form': form, 'goals': goals})

    def post(self, request):
        username = None
        password1 = None
        password2 = None
        email = None
        role = None
        success = None
        form = AddUserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']

            user = User.objects.create_user(username=username, email=email, password=password1)
            addUser = form.save(commit=False)
            addUser.save()

            form = AddUserForm()
        goals = ScrumyUser.objects.all()
        context = {'form': form, 'username': username, 'password1': password1, 'password2': password2, 'email': email, 'role': role, 'goals': goals, 'success': success}
        return render(request, 'oshodiscrumy/add_user.html', context)


def add_task(request):
    user = request.user
    if request.method == 'POST':
        form = AddTaskForm(request.POST)

        if form.is_valid():
            get_user = ScrumyUser.objects.get(username=user)
            get_Status = GoalStatus.objects.get(pk=get_user.role)

            addTask = ScrumyGoals.objects.create(
                goals = form.cleaned_data.get('goals'),
                goal_status = get_Status, 
                scrumy_user = get_user
                )
            return HttpResponse()

    else:
        form = AddTaskForm()
        all_user = ScrumyUser.objects.all()
    context = {
        'form': form,
        'user': user,
        'all_user': all_user
    }        
    return render(request, 'oshodiscrumy/add_task.html', context)

def move_task(request):
    user = request.user
    get_user = ScrumyUser.objects.get(username = user)
    get_Status = GoalStatus.objects.all()
    if request.method =='POST':
        form = AddTaskForm(request.POST)
        new_goal = request.POST['goal']

        if user.has_perm("oshodiscrumy.move_from_DT_to_verify") and GoalStatus.objects.get(pk = 2) == ScrumyGoals.objects.get(goals = request.POST['goal']).goal_status:
            move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
            move_task.goal_status = GoalStatus.objects.get(pk =3)
            move_task.save()
        elif user.has_perm("oshodiscrumy.move_from_WG_to_DT") and GoalStatus.objects.get(pk=1) == ScrumyGoals.objects.get(goals = request.POST['goal']).goal_status:
            move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
            move_task.goal_status = GoalStatus.objects.get(pk=2)
            move_task.save()
        elif user.has_perm("oshodiscrumy.move_from_verify_to_done") and GoalStatus.objects.get(pk=3) == ScrumyGoals.objects.get(goals = request.POST['goal']).goal_status:
            move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
            move_task.goal_status = GoalStatus.objects.get(pk=4)
            move_task.save()
        elif user.has_perm("okohscrumy.can_move_anywhere"):
            new_status = request.POST['new_status']
            move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
            move_task.goal_status = GoalStatus.objects.get(name=new_status)
            move_task.save()
        else:
            return HttpResponse("You do not have Permission to move this task")
        
        users_object = ScrumyUser.objects.all()
        context = { 'users_object': users_object}
        return render(request, 'oshodiscrumy/index.html', context)
    else:
        all_status = GoalStatus.objects.all()
        all_goals = ScrumyGoals.objects.all()
        weekly_goals = ScrumyGoals.objects.filter(goal_status = 1)
        daily_goals = ScrumyGoals.objects.filter(goal_status = 2)
        verify = ScrumyGoals.objects.filter(goal_status = 3)
        context = {
            'all_goals': all_goals,
            'all_status': all_status,
            'weekly_goals': weekly_goals,
            'daily_goals': daily_goals,
            'verify': verify
        }
    return render(request, 'oshodiscrumy/move_task.html', context)
    