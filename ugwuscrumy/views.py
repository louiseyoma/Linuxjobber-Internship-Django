from django.shortcuts import render
from django.http import HttpResponse
from ugwuscrumy.models import ScrumyUser,ScrumyGoals,GoalStatus
from . import forms


# Create your views here.
def index(request) :
    daily=GoalStatus.objects.get(status_name='daily target')
    query=ScrumyGoals.objects.filter(goal_status=daily.id)
    users=ScrumyUser.objects.all()
    users_dict={'user1':users}
    no_users=users.count()
    return HttpResponse(no_users)
    #return render(request,'ugwuscrumy/index.html',context=(users_dict)



def move_goal(request,task_id):
    query=ScrumyUser.objects.get(id=task_id)
    return HttpResponse(query)


def add_user(request):
    new_user_form=forms.NewUser()
    if request.method=='POST':
        form=forms.NewUser(request.POST)
        if form.is_valid:
            form.save(commit=True)
            total_users=ScrumyUser.objects.all()
            output = ', '.join([q.username for q in total_users])
            return HttpResponse(output)
    return render(request,'ugwuscrumy/add_user.html',{'form':new_user_form})
