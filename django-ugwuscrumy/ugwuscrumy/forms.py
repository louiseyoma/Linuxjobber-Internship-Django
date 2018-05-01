from django import forms
from ugwuscrumy.models import ScrumyUser


class NewUser(forms.ModelForm):
    class Meta:
        model=ScrumyUser
        fields="__all__"
