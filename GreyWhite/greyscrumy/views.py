from django.shortcuts import get_object_or_404,render

# Create your views here.
# from django.db.models.functions import Coalesce
from django.views.generic import TemplateView
from django.views import generic
from .models import ScrumyGoals, ScrumyUser, GoalStatus
from .form import UserForm



class IndexView(generic.ListView):
    template_name = 'greyscrumy/index.html'
    context_object_name = 'goals'


    def get_queryset(self):
    
        return ScrumyGoals.objects.all()


def Move_Goal(request, task_id):
    goals = get_object_or_404(ScrumyGoals, pk=task_id)
    return render(request, 'greyscrumy/details.html', {'goals': goals})



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





