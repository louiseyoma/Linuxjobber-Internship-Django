from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddUser, AddTask, ChangeGoalStatus
from .models import ScrumyGoals, ScrumyUser, GoalStatus
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
	new_user = ScrumyUser.objects.all()
	

	#user_details = ScrumyUser.objects.get(user_name='bilard')
	#userTarget = user_details.scrumygoals_set.all()
	another_user_list = ScrumyUser.objects.count()
	i = 1
	userTarget = ScrumyGoals.objects.filter(user_id=i).filter(status_id__exact=1)
	userTarget1 = ScrumyGoals.objects.filter(user_id=i+1).filter(status_id__exact=2)
	userTarget2 = ScrumyGoals.objects.filter(user_id=3).filter(status_id__exact=1)
	userTarget3 = ScrumyGoals.objects.filter(user_id=4).filter(status_id__exact=3)
	userTarget4 = ScrumyGoals.objects.filter(user_id=5).filter(status_id__exact=4)


	context = {'new_user': new_user, 'userTarget':userTarget, 'userTarget1':userTarget1, 'userTarget2':userTarget2, 'userTarget3':userTarget3,'userTarget4':userTarget4 }


	return render(request, 'osinuluscrumy/index.html', context)

def add_task(request):
	addtaskform = AddTask()
	context = {'form': AddTask}

	if request.method == 'POST':
		# creat an instance of add task form
		addtaskform = AddTask(request.POST)
		#check if the formis valid
		if addtaskform.is_valid():
			#saves the valid form to the database
			addtaskform.save()
			return redirect('index')
		else:
			return HttpResponse(addtaskform)
	return render(request, 'osinuluscrumy/add_task.html', context)

def add_user(request):
	adduserform = AddUser()
	context = {'form': AddUser}
	#if this is a post request we need to process the data
	if request.method == 'POST':
		# created a form instance and saved it with the users data
		adduserform = AddUser(request.POST)
		#checks if the form is valid
		if adduserform.is_valid():
			#saves the valid form to the database
			adduserform.save()
			return redirect('index')
		else:
			return HttpResponse(adduserform)
			#adduserform = AddUser()
	return render(request, 'osinuluscrumy/add_user.html', context)


def move_task(request, task_id):
	task = ScrumyGoals.objects.get(pk=task_id)
	changegoalstatusform = ChangeGoalStatus()
	context = {'form': ChangeGoalStatus}
	if request.method =='POST':
		changegoalstatusform = ChangeGoalStatus(request.POST, instance = task) 
		if changegoalstatusform.is_valid():
			changegoalstatusform.save()
			return redirect('index')
		else:
			return HttpResponse(changegoalstatusform)
	return render(request, 'osinuluscrumy/move_task.html', context)

"""def register(request):
	adduserform = AddUser()
	context = {'form': AddUser}
	return render(request, 'osinuluscrumy/add_user.html', context)"""