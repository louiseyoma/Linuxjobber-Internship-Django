from django.shortcuts import get_object_or_404, render
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import ListView
# Create your views here.
#view for index .html
def home(request):
    user = ScrumyUser.objects.get(id=1)
    user1 = ScrumyUser.objects.get(id=10)
    user2 =ScrumyUser.objects.get(id=3)
    user3 = ScrumyUser.objects.get(id=8)
    user4 = ScrumyUser.objects.get(id=9)
    goals= ScrumyUser.objects.filter(id=1)
    goals1=ScrumyUser.objects.filter(id=10)
    goals2=ScrumyUser.objects.filter(id=3)
    goals3=ScrumyUser.objects.filter(id=8)
    goals4=ScrumyUser.objects.filter(id=9)

    return render(request, 'oderascrumy/index.html',{'user': user, 'user1':user1 , 'user2':user2, 'goals':goals,
        'user3':user3, 'user4':user4, 'goals1':goals1, 'goals2':goals2,'goals3':goals3 ,'goals4':goals4})


    """newsize = ScrumyUser.objects.all()
    
    for users in newsize:
        count = ScrumyUser.objects.count()
        size=ScrumyUser.objects.filter(id__in=range(1,count))
        try:
            filtered_users=ScrumyUser.objects.get(id__exact=1)
        except ScrumyUser.DoesNotExist:
            raise Http404('USER DOES NOT EXIST IN THE DATABASE')
            #sizes = ScrumyUser.objects.filter(id=1)
            #return render(request,'oderascrumy/index.html',{'sizes':newsize})
        return render(request, 'oderascrumy/index.html',{'user':filtered_users})"""

    

def goals(request,pk):
    #goal = ScrumyGoals.objects.all()
    #return HttpResponse(goal)
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        form = AddTaskForm()
    return render(request, 'oderascrumy/goal.html', {'form': form})

def move_goals(request,pk):
    if request.method == 'POST':
        form = ChangeTaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        form = ChangeTaskForm()
    return render(request, 'oderascrumy/task.html', {'form': form})
    #task=ScrumyGoals.objects.all()
    #return render(request, 'oderascrumy/task.html',{'ad_task':task})
    

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        add=ScrumyUser.objects.create(name='',location='',email='',roles='')
        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        form = AddUserForm()
    return render(request, 'oderascrumy/user.html', {'form': form})
    #add=ScrumyUser.objects.create(name='debbie',location='lagos',email='debbieyahoo.com',roles='')
    #add.save()
    #users=ScrumyUser.objects.all()
    #for names in users:
        #pass
    #return render(request, 'oderascrumy/user.html',{'ad_user':users})
class ScrumyUserList(ListView):
    def listv(request):
        model = ScrumyUser
        #return render(request, 'oderascrumy/userlist.html', {'list': model})
