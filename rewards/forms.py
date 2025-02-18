from django import forms
from .models import Inventory, FrameAva, FrameChat


class InventForm(forms.ModelForm):
<<<<<<< HEAD
    chat = forms.ModelChoiceField(queryset=FrameChat.objects.all(), widget=forms.RadioSelect, label="Khung chat")
    ava = forms.ModelChoiceField(queryset=FrameAva.objects.all(),widget=forms.RadioSelect, label="Khung avatar")

    class Meta:
        model = Shop
        fields = ['chat', 'ava']
=======
    class Meta:
        model = Inventory
        fields = ['user']
>>>>>>> lab


# class ShopForm(forms.ModelForm):
#     chat = forms.ModelChoiceField(queryset=FrameChat.objects.all(), widget=forms.RadioSelect, label="Khung chat")
#     ava = forms.ModelChoiceField(queryset=FrameAva.objects.all(),widget=forms.RadioSelect, label="Khung avatar")

#     class Meta:
#         model = Shop
#         fields = ['chat_frames', 'ava_frames']