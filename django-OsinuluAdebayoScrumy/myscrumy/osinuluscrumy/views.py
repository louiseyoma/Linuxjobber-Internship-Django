from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddUser
from .models import ScrumyGoals, ScrumyUser, GoalStatus
# Create your views here.

def index(request):
	new_user = ScrumyUser.objects.all()
	context = {'new_user': new_user}
	#output = ' , '.join([q.user_name for q in new_user])
	#return HttpResponse(output)
	return render(request, 'osinuluscrumy/index.html', context)

def add_task(request, task_id):
	new_task = ScrumyGoals.objects.filter(status_id_id=task_id)
	second_output = ' ,'.join([q.user_goals for q in new_task])
	return HttpResponse(second_output)

def add_user(request):
	#if this is a post request we need to process the data
	if request.method == 'POST':
		# created a form instance and saved it with the users data
		adduserform = AddUser(request.POST)
		#checks if the form is valid
		if adduserform.is_valid():
			#saves the valid form to the database
			adduserform.save()
		else:
			return HttpResponse(adduserform)
			#adduserform = AddUser()
	return render(request, 'osinuluscrumy/index.html')


def register(request):
	adduserform = AddUser()
	context = {'form': AddUser}
	return render(request, 'osinuluscrumy/register.html', context)