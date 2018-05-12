from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser, ScrumyGoals
from django.shortcuts import render

# Create your views here.
def index(request):
    all_users = ScrumyUser.objects.all()
    context = {'all_users': all_users}
    return render(request, 'talabiscrumy/index.html', context)

def move_goal(request, task_id):
    task = ScrumyGoals.objects.get(pk=task_id)
    return HttpResponse("This is task %s. " % task)

def add_user(request, username, password, role):
    new_user = ScrumyUser(username=username, password=password, role=role)
    #save in db
    new_user.save()
    all_users = ScrumyUser.objects.all()
    output = ','.join([user.username for user in all_users])
    return HttpResponse(output)
    
