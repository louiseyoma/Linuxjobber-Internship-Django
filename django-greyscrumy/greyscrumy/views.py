from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView, View
from django.views import generic

from .models import ScrumyGoals, ScrumyUser, GoalStatus
from .form import UserForm, TaskForm


def index(request):

    users = ScrumyUser.objects.all()

    return render(request, 'greyscrumy/index.html', {'users': users})
    # ids = ScrumyUser.objects.values_list('id', flat=True)
    # temp = []
    # for i in ids:
    #     # goals = ScrumyGoals.objects.filter(goal_type = 'WG').filter(user_id_id = i)
    #     temp1 = get_object_or_404(ScrumyUser, pk = i)
    #     temp.append(temp1)
    
    #     try:
    #         goals = temp.scrumygoals_set.filter(goal_type = 'WG')
    #     except (KeyError, ScrumyGoals.DoesNotExist):
    #         return render(request, 'greyscrumy/index.html', {'error': 'ScrumyGoals for ScrumyUser not found' }) 
    #     else:
    #         return render(request, 'greyscrumy/index.html', {'goals': goals, 'ids':ids, 'temp': temp })

class Add_Task(TemplateView):
    def get(self, request):
        form = TaskForm()
        goals = ScrumyGoals.objects.all()
        return render(request, 'greyscrumy/add_task.html', {'form': form, 'goals': goals})
        
    def post(self, request):
        user = None
        status_id = None
        goalType = None
        task = None
        date_created = None
        date_updated = None
        success = None

        form = TaskForm(request.POST or None)
        if form.is_valid():
            success = 'Successful'
            form.save()

            user_id = form.cleaned_data['user_id']
            status_id = form.cleaned_data['status_id']
            goal_type = form.cleaned_data['goal_type']
            goal_description = form.cleaned_data['goal_description']
            date_created = form.cleaned_data['date_created']
            date_updated = form.cleaned_data['date_updated']
          
            form = TaskForm()
        goals = ScrumyGoals.objects.all()
        args = {'form': form, 'user': user, 'status_id': status_id, 'goalType': goalType, 'task': task,'date_created': date_created, 'date_updated': date_updated, 'goals': goals, 'success': success}

        return render(request, 'greyscrumy/add_task.html', args)



# class Add_Task(TemplateView):


#     def get(self, request):
#         form = TaskForm()

#         goals = ScrumyGoals.objects.all()

#         return render(request, 'greyscrumy/add_task.html', {'form':form, 'goals': goals })

#     def post(self, request):

#         form = TaskForm(request.POST)

#         if form.is_valid():

            
#             form.save()
#             # user = form.save(commit=False)
#             # success = 'Registered Successfully'
            
#             # newUser = ScrumyUser()
#             user_id = form.cleaned_data['user_id']
#             status_id = form.cleaned_data['status_id']
#             goal_type = form.cleaned_data['goal_type']
#             goal_description = form.cleaned_data['goal_description']
    

#             form = TaskForm()

#         goals = ScrumyGoals.objects.all()
    
#         args = {'form': form, 'goals': goals}

#         return render(request, 'greyscrumy/add_task.html', args)


def Move_Task(request, task_id):
    goals = get_object_or_404(ScrumyGoals, pk=task_id)
    return render(request, 'greyscrumy/move_task.html', {'goals': goals})



class Add_User(TemplateView):


    def get(self, request):
        form = UserForm()

        goals = ScrumyUser.objects.all()

        return render(request, 'greyscrumy/adduser.html', {'form':form, 'goals': goals })

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():

            success = 'Registered Successfully'
            form.save()

            name = form.cleaned_data['fullname']
            role = form.cleaned_data['role']

            form = UserForm()
        goals = ScrumyUser.objects.all()
       
        args = {'form': form, 'name': name, 'role': role, 'goals': goals, 'success': success}

        return render(request, 'greyscrumy/adduser.html', args)

