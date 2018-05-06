from django import forms
from .models import ScrumyUser,ScrumyGoals

class UserForm(forms.ModelForm):
   user_name  = forms.CharField(label='Email Address', max_length=50)
   role  = forms.CharField(label='User Role', max_length=50)

   class Meta:
       model = ScrumyUser
       fields = ('user_name', 'role')

class ChangeTaskStatusForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['status_id']

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = '__all__'
