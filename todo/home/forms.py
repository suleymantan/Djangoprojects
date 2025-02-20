from django import forms
from django.forms import ModelForm
from .models import ToDoList

from .models import *

class TodoForm(forms.ModelForm):
    

    class Meta:
        model = ToDoList
        fields = ['todo','commence','fin']
        widgets = {
            'todo': forms.TextInput(attrs={"class": "form-control form-group", "required:": "", "placeholder": "Enter Task"}),
            'commence':forms.DateInput(attrs={"class": "form-control form-group", "required:": "", "placeholder": "yyyy-mm-dd"}),
            'fin':forms.DateInput(attrs={"class": "form-control form-group", "required:": "", "placeholder": "yyyy-mm-dd"})
        
        }