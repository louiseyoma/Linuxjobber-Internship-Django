from django import forms
from .models import ScrumyUser

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

