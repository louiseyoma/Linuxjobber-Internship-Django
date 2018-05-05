from django import forms
from .models import User, Goal

# add new user form class
class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'role']

# add task form class
class AddTask(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['user', 'task', 'status']

# move task form class
class MoveTask(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['user', 'task', 'status']