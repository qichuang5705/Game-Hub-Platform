from django import forms
from .models import Comment, Game, Genre
import os, zipfile
from django.conf import settings
from django.utils.text import slugify
import uuid
from django.contrib import messages
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('words',)
        widgets = {
            'words': forms.Textarea(attrs={ 
                'class': 'comment-textarea',
                'placeholder': 'Nhập bình luận của bạn...'
            })
        }

class UpGameForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        error_messages={'required': 'Bạn cần chọn ít nhất một thể loại.'},
    )
    image = forms.ImageField(required=True)
    file = forms.FileField(required=True)
    class Meta:
        model = Game
        fields = ('name', 'genres', 'ApiLD', 'description', 'image', 'file')

    def clean_genres(self):
        genres = self.cleaned_data.get('genres')
        if not genres or genres.count() == 0:
            raise forms.ValidationError("Bạn cần chọn ít nhất một thể loại.")
            messages.error(request,"Bạn cần chọn ít nhất một thể loại.")
        return genres


    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            file_name = os.path.basename(file.name)
            file_extension = os.path.splitext(file_name)[1].lower()

            if file_extension not in ['.html', '.zip']:
                raise forms.ValidationError("File upload phải là 'index.html' hoặc file '.zip'")
                
            
    
            if file_extension == '.html' and file_name.lower() != 'index.html':
                raise forms.ValidationError("File HTML phải có tên là 'index.html'")
            
            if file_extension == '.zip':
                try:
                    with zipfile.ZipFile(file, 'r') as zip_ref:
                        file_list = zip_ref.namelist()  # Lấy danh sách file trong zip
                        if 'index.html' not in file_list:
                            raise forms.ValidationError("Phải đăng tải file 'index.html' là con cấp 1 của file .zip")
                except zipfile.BadZipFile:
                    raise forms.ValidationError("File .zip không hợp lệ hoặc bị lỗi.")
        return file

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image == self.instance.image.name:
            print("báo lỗi trùng tên")
            forms.ValidationError("Đổi lại tên tệp image")
        elif image:
      
            _, image_extension = os.path.splitext(image.name)

            new_image_name = f"{uuid.uuid4().hex}{image_extension.lower()}"
        
            image.name = os.path.join('image', new_image_name)

        return image 

    