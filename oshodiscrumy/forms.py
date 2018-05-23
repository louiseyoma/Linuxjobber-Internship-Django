from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import ScrumyUser, ScrumyGoals, GoalStatus

class AddUserForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Enter Email', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    role = forms.CharField(label='Choose User Role',max_length=1, widget=forms.Select(choices=ScrumyUser.ROLES, attrs={'class': 'form-control'}))

    class Meta:
        model = ScrumyUser
        fields = ['username', 'password1', 'password2', 'email', 'role']



class AddTaskForm(forms.ModelForm):
    goal_status = forms.ModelChoiceField(label='Enter Goal Status', queryset=GoalStatus.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    goals = forms.CharField(label='Enter Goals', widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = ScrumyGoals
        fields = ['goal_status', 'goals']

class ChangeTaskStatusForm(forms.ModelForm):
    class Meta:
        model = GoalStatus
        fields = ['name']




# class UserRegistration(UserCreationForm):
#     email=forms.CharField(max_length=254, required=True,widget=forms.EmailInput())
#     username=forms.CharField(max_length=100,required=True)
#     class Meta:
#         model = User
#         fields = '__all__'
