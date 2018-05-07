from django.forms import ModelForm
from django import forms
from .models import ScrumyUser, ScrumyGoals, GoalStatus


class AddUserForm(forms.ModelForm):
    class Meta:
        model = ScrumyUser
        fields = ('name', 'location','email','roles')

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ('user_name', 'status_id','goal_type','goal_status')

class ChangeTaskForm(forms.ModelForm):
    class Meta:
        model = GoalStatus
        fields = ('title', 'task_id','description','status', 'verified_by') 





