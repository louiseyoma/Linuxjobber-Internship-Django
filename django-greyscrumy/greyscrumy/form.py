from django.contrib.auth.models import User
from django import forms
from .models import ScrumyUser, ScrumyGoals

class UserForm(forms.ModelForm):
    fullname  = forms.CharField(label='Enter User Name', max_length=100)
    role  = forms.CharField(label='Enter User Role', max_length=100)

    class Meta:
        model = ScrumyUser

        fields = ('fullname', 'role')

   


class TaskForm(forms.ModelForm):
   
    # user_id = form.cleaned_data['user']
    # status_id = form.cleaned_data['status_id']
    

    goal_type = forms.CharField(label='Enter goal type e.g "WG / DT"', max_length=10)
    goal_description = forms.CharField(label='Enter goal description', max_length=500)
    date_created = forms.DateField(label='Enter Date')
    date_updated = forms.DateField(label='Enter date last updated')
    
    
    class Meta:
        model = ScrumyGoals
        fields = ('user_id', 'status_id','goal_type', 'goal_description', 'date_created', 'date_updated')


