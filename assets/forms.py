from django import forms
from .models import asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = asset
        fields = ['title', 'price', 'type', 'description', 'quantifier', 'thumnail','file']
    def save(self, commit=True, user=None):  # Thêm user vào save()
        asset = super().save(commit=False)
        if user:
            asset.User = user  # Gán user nếu truyền vào
        if commit:
            asset.save()
        return asset
        
