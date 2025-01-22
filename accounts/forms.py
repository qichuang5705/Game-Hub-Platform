from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
    )
    requested_role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,  # Tải các lựa chọn từ model CustomUser
        label="Select Role",
        widget=forms.Select,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'requested_role']  # Bao gồm trường requested_role

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loại bỏ help texts khỏi tất cả các trường
        for field in self.fields.values():
            field.help_text = ""
    
    def clean(self):
        cleaned_data = super().clean()
        requested_role = cleaned_data.get('requested_role')

        # Kiểm tra nếu requested_role không hợp lệ
        if requested_role not in dict(CustomUser.ROLE_CHOICES):
            raise forms.ValidationError({'requested_role': 'Invalid role selection.'})

        return cleaned_data
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class RoleUpgradeRequestForm(forms.Form):
    requested_role = forms.ChoiceField(
        choices=[(CustomUser.ROLE_DEVELOPER, 'Developer'), (CustomUser.ROLE_DESIGNER, 'Designer')],
        label="Request Role Upgrade",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loại bỏ help_text mặc định từ tất cả các trường
        for field in self.fields.values():
            field.help_text = ""
    
    def clean_requested_role(self):
        """Kiểm tra sự hợp lệ của requested_role"""
        requested_role = self.cleaned_data.get('requested_role')
        
        if requested_role not in [CustomUser.ROLE_DEVELOPER, CustomUser.ROLE_DESIGNER]:
            raise forms.ValidationError('Invalid role selection.')
        
        return requested_role

    def clean(self):
        """Phương thức này sẽ kiểm tra nếu trường requested_role không được chọn"""
        cleaned_data = super().clean()
        requested_role = cleaned_data.get('requested_role')

        if not requested_role:
            raise forms.ValidationError({'requested_role': 'You must select a role to upgrade.'})

        return cleaned_data
    

class FormInfor(forms.ModelForm):
   class Meta:
        model = CustomUser 
        fields = ('first_name', 'last_name', 'email')

