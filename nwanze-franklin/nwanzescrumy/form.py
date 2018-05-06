from django import forms
from django.core.exceptions import ValidationError
import json
from nwanzescrumy.models import *
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    user_name = forms.CharField(label='User name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = ScrumyUser
        fields = ['first_name', 'last_name', 'user_name', 'email', 'password']

    def clean_email(self):
        data = self.cleaned_data['email']
        
        if ScrumyUser.objects.filter(email=data).count() > 0:
            raise ValidationError(_('Email Already Exists'))
        return data
    
    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        
        if ScrumyUser.objects.filter(user_name=data).count() > 0:
            raise ValidationError(_('user name Already Exists'))
        return data

class TaskForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': "6",'class':'form-control' }))

    class Meta:
        model = Task
        fields = ['description']
     
    def clean_description(self):
        data = self.cleaned_data['description']
        
        if len(data.strip()) < 10:
            raise ValidationError(_('Description is short'))
        return data


class ChangeTaskStatusForm(forms.Form):
    status = [(obj.id, obj.status) for obj in GoalStatus.objects.all()]
    CHOICES= (
            status
        )
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    goal = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES)
    
    class Meta:
        model = Task
        fields = ['description']
    
