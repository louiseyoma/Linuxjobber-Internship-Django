from django.contrib.auth.models import User
from django import forms
from .models import ScrumyUser

class UserForm(forms.ModelForm):
   fullname  = forms.CharField(label='Enter User Name', max_length=100)
   role  = forms.CharField(label='Enter User Role', max_length=100)

   class Meta:
       model = ScrumyUser

       fields = ('fullname', 'role')

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']