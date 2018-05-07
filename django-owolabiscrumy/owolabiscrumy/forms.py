from django.forms import ModelForm
from .models import ScrumyUser, ScrumyGoals, GoalStatus
from django import forms


#Create your forms here

class AddUserForm(forms.ModelForm):
	full_name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)


	class Meta:
		model = ScrumyUser
		fields = ['full_name', 'email','role']


class AddTaskForm(forms.ModelForm):
	goals = forms.CharField(max_length=50)
	descriptions = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = ScrumyGoals
		fields = ['scrumyuser', 'goal_type', 'goals', 'descriptions']

