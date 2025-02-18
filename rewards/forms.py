from django import forms
from .models import TableRewards

class TableChat(forms.ModelForm):
    class Meta:
        model = TableRewards
        fields = ['framechat']