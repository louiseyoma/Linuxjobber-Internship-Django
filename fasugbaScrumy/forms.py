from .models import ScrumyUser, ScrumyGoals, ScrumyStatus
from django import forms


class ScrumyUserForm(forms.ModelForm):
	class Meta:
		model = ScrumyUser
		fields = [
			'first_name',
			'last_name',
			'email',
			'phone_no'
		]


class ScrumyGoalsForm(forms.ModelForm):
	class Meta:
		model = ScrumyGoals
		fields = [
			'goals'
		]
			

class ScrumyStatusForm(forms.ModelForm):
	class Meta:
		model = ScrumyStatus
		fields = [
			'name'
		]





