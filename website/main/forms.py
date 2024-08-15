from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *



class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.EmailField(label='Email', max_length=254,required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]

class TaskForm(ModelForm):
   class Meta:
      model = Task
      fields = ['title', 'completed']
      widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            
        }
class DefaultTaskForm(ModelForm):
   class Meta:
      model = DefaultTask
      fields = ['title']
      widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            
        }



