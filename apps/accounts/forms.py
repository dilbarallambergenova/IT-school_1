from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('username','first_name','last_name','gender','phone','email','date_of_birth','address')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('username','first_name','last_name','gender','phone','email','date_of_birth','address')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        