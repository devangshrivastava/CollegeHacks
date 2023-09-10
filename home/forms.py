from django.forms import ModelForm, TextInput, CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import myuploadfile



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UploadAllFiles(ModelForm):
    class Meta:
        model = myuploadfile
        fields = '__all__'
        widgets = {
            'f_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                # 'placeholder': 'Name'
                }),
            'course': forms.Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Course'
                }),
            'batch': forms.Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Batch'
                }),
            'type': forms.Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Type'
                })
        }