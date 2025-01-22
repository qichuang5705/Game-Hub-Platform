from django import forms
from .models import Comment, Game


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('words',)

class UpGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'genre', 'description', 'image', 'file')


