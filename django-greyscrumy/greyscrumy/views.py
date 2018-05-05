from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
# from django.db.models.functions import Coalesce
from django.views.generic import TemplateView, View
from django.views import generic

from .models import ScrumyGoals, ScrumyUser, GoalStatus
from .form import UserForm, LoginForm

def index(request):

    hello = 'Hello World'
    daily_target = ScrumyGoals.objects.filter(goal_type='WG')
    # total_users = ScrumyUser.objects.all().count()
    ids = ScrumyUser.objects.values_list('id', flat=True)
    ids = max(ids)
    
   
    
    for i in range(1, ids):
        goals = ScrumyGoals.objects.filter(goal_type = 'WG').filter(user_id_id = i)
        # temp = get_object_or_404(ScrumyUser, pk=i)
        # if temp:
        #     goals = temp.scrumygoals_set.filter(goal_type = 'WG')
        return render(request, 'greyscrumy/index.html', {'goals': goals, 'ids':ids })

class Add_Task(generic.ListView):
    template_name = 'greyscrumy/add_task.html'
    context_object_name = 'goals'


    def get_queryset(self):
        return ScrumyGoals.objects.all()


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


# class RegisterFormView(View):
#     form_class = LoginForm()
#     template_name = 'greyscrumy/register.html'

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user.set_password(password)
#             user.save()


#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('greyscrumy:index')

#         return render(request, self.template_name, {'form', form})



            

