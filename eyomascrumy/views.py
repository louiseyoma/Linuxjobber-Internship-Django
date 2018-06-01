from django.shortcuts import render, HttpResponse
from .models import ScrumyGoals, ScrumyUser
from django.http import Http404


def homepage(request):
	user = ScrumyUser.objects.get(pk=1)
	tasks = user.scrumygoals_set.all() 
	return render(request, "eyomascrumy/home.html", {'username':user,'goals':tasks})


def findUser(request, username):
	try:
		user = ScrumyUser.objects.get(userName = username)
	except ScrumyUser.DoesNotExist:
		raise Http404("User does not exist")
	return render(request, "eyomascrumy/users.html", {"user":user})

def addTask(request,usersView):
	return HttpResponse("Hello %s please edit or add a new task" % usersView )

def addUser(request):

	if request.method == 'POST':
		user = request.POST.get('username')
		if user is '':
			error_message = 'Please username cannot be empty'
			return render(request, "eyomascrumy/add_user.html", {'error_message':error_message})
		else:
			b=ScrumyUser(userName = user)
			b.save()
			x=ScrumyUser.objects.get(userName=user)
			return HttpResponse(x)
	else:
		return render(request, "eyomascrumy/add_user.html")

		
	
	
	'''
	user = ScrumyUser(userName='mike')
	user.save()
	users = ScrumyUser.objects.all()
	output = ', '.join([eachuser.userName for eachuser in users])
	return HttpResponse(output)
	'''