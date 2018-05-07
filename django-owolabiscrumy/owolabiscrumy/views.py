from django.shortcuts import redirect
from django.http import HttpResponse
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from .forms import AddUserForm, AddTaskForm
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404
# Create your views here.

def index(request):
	everyuser=ScrumyUser.objects.all()
	goals=ScrumyUser.objects.filter(scrumygoals__goal_type='WG')

	
	return render(request, 'scrum/index.html', {'everyuser':everyuser, 'goals':goals})




def move_task(request, task_id):
    goals=ScrumyGoals.objects.get(pk=task_id)
    print(goals.descriptions)
    if request.method=='POST':
        form=AddTaskForm(request.POST, instance=goals)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=AddTaskForm(instance=goals)

    return render(request,'move_task.html',{'instance':goals, 'forms':form})
	


def add_task(request):
    if request.method=='POST':
        form=AddTaskForm(request.POST)

        if form.is_valid():
            addtask=form.save(commit=False)
            addtask.save()

            addtasks=ScrumyGoals.objects.create(
                goals=form.cleaned_data.get('goals'),
                descriptions=form.cleaned_data.get('descriptions'),
                scrumyuser=form.cleaned_data.get('scrumyuser'),
                goal_type=form.cleaned_data.get('goal_type')
            )
            return redirect('index.html')
    else:
        form=AddTaskForm(request.POST)
    return render(request,'scrum/add_task.html',{'forms':form})

def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()

            users=ScrumyUser.objects.create(
                full_name=form.cleaned_data.get('full_name'),
                email=form.cleaned_data.get('email')
                
            )
            return redirect('scrum/index')
    else:
        form=AddUserForm(request.POST)
    return render(request,'scrum/add_user.html',{'forms':form})

def details(request):
    return HttpResponse("You are looking at details")



    #user = ScrumyUser(full_name = 'Tope')
    #user.save()
    #users = ScrumyUser.objects.all()
    #output = ', '.join([eachuser.full_name for eachuser in users])
    #return HttpResponse(output)


    #users = ScrumyUser.objects.all()
	#output = ','.join([s.first_name for s in users])
	#goals= ScrumyGoals.objects.filter(goal_type='DT')


#def index(request):results = ScrumyUser.objects.count()
	#context = {'results': results,}
	#return render(request, 'scrum/index.html', context )
	
	#goalz=user.scrumygoals_set.all()
			#ctx = {"goalz": goalz,'user':user}
			#goals=list(ctx)


	
	#except user.DoesNotExist as e:
	#	return show_error(request,e.__str__()) 
	#number_of_users = ScrumyUser.objects.count()
	#for i in range(1,number_of_users):
	#		user=ScrumyUser.objects.all()
	#		context= {'user' : user}