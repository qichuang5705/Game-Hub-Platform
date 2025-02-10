from django import forms
from .models import asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = asset
        fields = ['title', 'price', 'type', 'description', 'quantifier', 'thumnail']
