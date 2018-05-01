from django import forms
from .models import ScrumyUser

class UserForm(forms.ModelForm):
   fullname  = forms.CharField(label='Enter User Name', max_length=100)
   role  = forms.CharField(label='Enter User Role', max_length=100)

   class Meta:
       model = ScrumyUser

       fields = ('fullname', 'role')