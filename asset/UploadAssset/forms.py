from django import forms
from .models import asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = asset
        fields = ['price', 'type', 'description','quantifier','title','thumnail']
