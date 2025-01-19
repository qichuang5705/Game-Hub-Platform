from django import forms
from .models import Comment, Game
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.ModelForm):
    words = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Comment
        fields = ('words',)

class UpGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'genre', 'description', 'image', 'file', 'game_type')