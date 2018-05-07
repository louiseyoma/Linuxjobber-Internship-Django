from django import forms
from .models import ScrumyUser, ScrumyGoal


class UserForm(forms.ModelForm):
    class Meta:
        model = ScrumyUser
        fields = ['Name', 'Age', 'Username', 'Email', 'Role']


class GoalForm(forms.ModelForm):
    #user_id = form.cleaned_data['user']

    class Meta:
        model = ScrumyGoal
        fields = ['title', 'Goal_type', 'Desciption', 'user']
