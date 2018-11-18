from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = ('User', {'fields': ('username','password','name','type','mobile','email','address','bloodgroup1','bloodgroup2','bloodgroup3','bloodgroup4','bloodgroup5','bloodgroup6','bloodgroup7','bloodgroup8',)}),
    list_display = ['username','name','email','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
