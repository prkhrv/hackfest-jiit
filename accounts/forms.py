from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','name','type','mobile','address','bloodgroup1','bloodgroup2','bloodgroup3','bloodgroup4','bloodgroup5','bloodgroup6','bloodgroup7','bloodgroup8')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','name','type','mobile','address','bloodgroup1','bloodgroup2','bloodgroup3','bloodgroup4','bloodgroup5','bloodgroup6','bloodgroup7','bloodgroup8')
