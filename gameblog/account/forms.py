from django.contrib.auth.forms import UserCreationForm
from .models import *  
from django import forms

class FormUser(UserCreationForm):
   class Meta:
        model = User  # Sử dụng mô hình tùy chỉnh
        fields = ('username', 'password1', 'password2')



class APIin4(forms.ModelForm):
   class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email')

