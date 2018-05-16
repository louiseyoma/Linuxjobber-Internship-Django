import datetime

from django.db.models.functions import Trunc
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from adesokanscrumy.models import GoalStatus, ScrumyGoals

from .models import (GoalStatusManager, GoalStatusQueryset, ScrumyGoalsManager,
                     ScrumyGoalsQueryset, ScrumyUser)


def index(request):
    #queryset= ScrumyUser.objects.all() 
    
    
    person = ScrumyUser.objects.get(id)
    allusers= ScrumyUser.objects.all()
    
    try:
        go = ScrumyUser.objects.get(id=4)
        print(go)
    except ObjectDoesNotExist:
        print ("Either the entry or blog doesn't exist.")
        

    context= {
        #"object_list":queryset,
        "name": person.username,
        "person":person,   
        "allusers": allusers,  
        "counter": allusers.count(),
        #"task_id": task_id,
                }
    return render(request,'adesokanscrumy/templates/index.html', context)

   

def home(request):
    instance= GoalStatus.objects.get(id=1)
    
    

    context= {
        "title" :instance.date_completed,
        "instance": instance,
    }
    return render(request,'adesokanscrumy/templates/one.html', context)
   

def move_goal(request, task_id):
    goalinstance= GoalStatus.objects.get(id=1)
    

    context= {
        "newtitle" :goalinstance.date_completed,
        "goalinstance": goalinstance,
    }
    return render(request,'adesokanscrumy/templates/movegoal.html', context)


def add_user(request ):
        newuser =ScrumyUser()
        newuser.username= "babadaradara"
        newuser.gender="female"
        newuser.roles='QA'
        newuser.email="babao@gmail.com"
        newuser.date_registered= Trunc(datetime,"day")
        newuser.save()
        
    
        output ="this is the  ', '.join([eachuser.username for eachuser in ScrumyUser.objects.all()])"
        return HttpResponse(request,output)
