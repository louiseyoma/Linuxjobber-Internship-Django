from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import ScrumyUser, ScrumyGoals, ScrumyStatus
from .forms import ScrumyUserForm, ScrumyGoalsForm, ScrumyStatusForm
from django.contrib.auth.models import Group, Permission,User
from django.views import generic

# Create your views here.

def index1(request):
	size = ScrumyUser.objects.all()
	size = size.count()
	var = ScrumyUser.objects.filter(id__range=(1,size))
	var3 = ScrumyUser.objects.get(id=4)
	try:
		var2 = ScrumyUser.objects.get(id=4)

	except ObjectDoesNotExist as e:
		return HttpResponse("The id no do not exist in database")

	else:
			context ={
			'var': var,
			'var2': var2,
			'var3': var3,
			'size': size
			}	
			return render(request, 'fasugbaScrumy/index.html', context)


def index(request):
	user = ScrumyUser.objects.get(id=2)
	userGoal = user.scrumygoals_set.filter(scrumy_status=1)
	context ={
			'user': user,
			'userGoal': userGoal			
			}	
	return render(request, 'fasugbaScrumy/index.html', context)
			

def add_user(request):
	if request.method == 'POST':
		form = ScrumyUserForm(request.POST)
	
		if form.is_valid():
			addUser = form.save(commit=False)
			addUser.save()
			return redirect('index')

	else:			
		form = ScrumyUserForm()
		context = {
		'form': form
	}	
	return render(request, 'fasugbaScrumy/add_user.html', context)


def add_task(request):
	if request.method == 'POST':
		form = ScrumyGoalsForm(request.POST)

		if form.is_valid():
			goalAdder= ScrumyUser.objects.get(pk=2)
			goalStatus=ScrumyStatus.objects.get(pk=1)

			addTask = ScrumyGoals.objects.create(
				goals = form.cleaned_data.get('goals'),
				scrumy_status = goalStatus, 
				scrumy_user = goalAdder
				)
			return redirect(index)

	else:
		form = ScrumyGoalsForm()
		user = request.user
	context = {
		'form': form,
		'user': user
	}		
	return render(request, 'fasugbaScrumy/add_task.html', context)



def move_task(request,task_id):
	getTask = ScrumyGoals.objects.get(pk = task_id)
	if request.method == 'POST':
		form = ScrumyGoalsForm(request.POST)
		user = request.user

		if user.has_perm("fasugbaScrumy.DT_to_verify") and ScrumyStatus.objects.get(pk=2) == ScrumyGoals.objects.get(pk = task_id).scrumy_status:
			move_task = ScrumyGoals.objects.get(pk = task_id)
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=3)
			move_task.save()
			return HttpResponse("The task has been successfully moved fro daily goals to verify ")

		elif user.has_perm("fasugbaScrumy.verify_t0_done") and ScrumyStatus.objects.get(pk=3) == ScrumyGoals.objects.get(pk = task_id).scrumy_status:
			move_task = ScrumyGoals.objects.get(pk = task_id)
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=4)
			move_task.save()
			return HttpResponse("The task has been successfully moved from verify to done")

		elif user.has_perm("fasugbaScrumy.WG_to_DT") and ScrumyStatus.objects.get(pk=1) == ScrumyGoals.objects.get(pk = task_id).scrumy_status:
			move_task = ScrumyGoals.objects.get(pk = task_id)
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=2)
			move_task.save()
			return HttpResponse("The task has been successfully moved from weekly goals to daily task")

		elif user.has_perm("fasugbaScrumy.anywhere_to_anywhere"):
			new_status = request.POST['new_status']
			move_task = ScrumyGoals.objects.get(pk = task_id)
			mmm = ScrumyStatus.objects.get(pk=4)
			move_task.scrumy_status = ScrumyStatus.objects.get(name=new_status)
			move_task.save()
			return HttpResponse("The task has been successfully moved")

		else:
			return HttpResponse("You do not have Permissionto move this task")


	else:
		form = ScrumyGoalsForm()
		weekly_status = ScrumyGoals.objects.filter(scrumy_status=1)
		all_status = ScrumyStatus.objects.filter(pk__range=(1,4))
		task = ScrumyGoals.objects.get(pk = task_id).scrumy_status
		status = ScrumyStatus.objects.get(pk=2)
		context = {
			'form': form,
			'getTask': getTask,
			'task': task,
			'status': status,
			'weekly_status': weekly_status,
			'all_status': all_status

		}	
	return render(request, 'fasugbaScrumy/move_task.html', context)




class goals_view(generic.ListView):

    template_name = 'fasugbaScrumy/goals_view.html'

    context_object_name = 'goals_object'



    def get_queryset(self):

        return ScrumyGoals.objects.all()