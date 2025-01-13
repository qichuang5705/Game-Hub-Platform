from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="",  # Ẩn help text
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        help_text="",  # Ẩn help text
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loại bỏ help texts khỏi tất cả các trường
        for field_name, field in self.fields.items():
            field.help_text = ""

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']