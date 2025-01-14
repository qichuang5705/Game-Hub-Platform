from django import forms
from .models import Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.ModelForm):
    words = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Comment
        fields = ('words',)

