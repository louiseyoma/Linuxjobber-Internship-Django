from django import forms
from .models import ScrumyUser, ScrumyGoals, GoalStatus

class AddUser(forms.ModelForm):
	class Meta:
		model = ScrumyUser
		fields = ['user_name', 'first_name', 'last_name', 'age']
		widgets = {
		'user_name': forms.TextInput(attrs={'placeholder': 'Username'}),
		'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
		'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
		'age': forms.NumberInput()
		}


class AddTask(forms.ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['user_id', 'status_id', 'user_goals']
		user_id = forms.ModelChoiceField(queryset=ScrumyUser.objects.all())
		status_id = forms.ModelChoiceField(queryset=GoalStatus.objects.all())
		widgets = {
		'user_goals': forms.TextInput(attrs={'placeholder': 'Enter your Goals'})
		}

class ChangeGoalStatus(forms.ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = ['status_id']
		status_id = forms.ModelChoiceField(queryset=GoalStatus.objects.all())

		