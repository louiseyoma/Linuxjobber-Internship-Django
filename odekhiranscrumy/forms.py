from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Password'}),
        }