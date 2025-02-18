from django import forms
from .models import Inventory, FrameAva, FrameChat, Shop

class InventForm(forms.ModelForm):
    framechat = forms.ModelChoiceField(
        queryset=FrameChat.objects.all(),
        widget=forms.RadioSelect,  
        empty_label=None,
     
    )
    frameava = forms.ModelChoiceField(
        queryset=FrameAva.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
    
    )

    class Meta:
        model = Inventory
        fields = ['chat', 'ava']


class ShopForm(forms.ModelForm):
    chat = forms.ModelChoiceField(queryset=FrameChat.objects.all(), widget=forms.RadioSelect, label="Khung chat")
    ava = forms.ModelChoiceField(queryset=FrameAva.objects.all(),widget=forms.RadioSelect, label="Khung avatar")

    class Meta:
        model = Shop
        fields = ['chat', 'ava']