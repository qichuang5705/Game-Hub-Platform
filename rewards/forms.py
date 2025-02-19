from django import forms
from .models import Inventory, FrameAvatar, FrameChat, Avatar, Chat

# class InventForm(forms.ModelForm):

#     frame_chat = forms.ModelChoiceField( queryset=FrameChat.objects.all(),  widget=forms.RadioSelect,  required=False,
#         label="Chọn Khung Chat")
#     frame_ava = forms.ModelChoiceField( queryset=FrameAvatar.objects.all(),  widget=forms.RadioSelect,  required=False,
#         label="Chọn Khung avatar")
#     class Meta:
#         model = Inventory
#         fields = ['avatar', 'chat']

class InventForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['avatar', 'chat']
        widgets = {
            'avatar': forms.RadioSelect(),
            'chat': forms.RadioSelect(),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            # Chỉ hiển thị Avatar và Chat mà user sở hữu
            self.fields['avatar'].queryset = Avatar.objects.filter(user=user)
            self.fields['chat'].queryset = Chat.objects.filter(user=user)


# class ShopForm(forms.ModelForm):
#     chat = forms.ModelChoiceField(queryset=FrameChat.objects.all(), widget=forms.RadioSelect, label="Khung chat")
#     ava = forms.ModelChoiceField(queryset=FrameAva.objects.all(),widget=forms.RadioSelect, label="Khung avatar")

#     class Meta:
#         model = Shop
#         fields = ['chat_frames', 'ava_frames']