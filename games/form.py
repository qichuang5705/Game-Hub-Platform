from django import forms
from .models import Comment, Game, Genre


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('words',)

class UpGameForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),  # Lấy tất cả thể loại từ cơ sở dữ liệu
        widget=forms.CheckboxSelectMultiple,  # Sử dụng checkbox để lựa chọn nhiều thể loại
    )

    class Meta:
        model = Game
        fields = ('name', 'genres', 'description', 'image', 'file')

