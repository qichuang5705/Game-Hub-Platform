from django import forms
from .models import Comment, Game, Genre
import os
from django.conf import settings
from django.utils.text import slugify
import uuid

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('words',)

class UpGameForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        error_messages={'required': 'Bạn cần chọn ít nhất một thể loại.'},
    )

    class Meta:
        model = Game
        fields = ('name', 'genres', 'description', 'image', 'file')

    def clean_genres(self):
        genres = self.cleaned_data.get('genres')
        if not genres or genres.count() == 0:
            raise forms.ValidationError("Bạn cần chọn ít nhất một thể loại.")
        return genres


    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            file_name = os.path.basename(file.name)
            file_extension = os.path.splitext(file_name)[1].lower()

            # Kiểm tra phần mở rộng
            if file_extension not in ['.html', '.zip']:
                raise forms.ValidationError("File upload phải là 'index.html' hoặc file '.zip'")
            
            # Kiểm tra tên nếu là file HTML
            if file_extension == '.html' and file_name.lower() != 'index.html':
                raise forms.ValidationError("File HTML phải có tên là 'index.html'")
            
            # Lấy tên file không có phần mở rộng
            file_name = os.path.splitext(file.name)[0]
            # Đường dẫn đầy đủ của thư mục dự kiến
            target_folder = os.path.join('games', 'file', file_name)

            # Kiểm tra nếu thư mục đã tồn tại
            if os.path.exists(os.path.join(settings.MEDIA_ROOT, target_folder)):
                raise forms.ValidationError(f"Tên file '{file_name}' đã trùng với một thư mục hiện có!")
        return file

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Lấy phần mở rộng và tên file
            image_name = os.path.basename(image.name)
            image_extension = os.path.splitext(image_name)[1].lower()

            # Đổi tên file ảnh
            new_image_name = f"{slugify(self.cleaned_data.get('name'))}_image_{uuid.uuid4().hex}{image_extension}"

           # Di chuyển file ảnh tới tên mới trong MEDIA_ROOT
            new_image_path = os.path.join(settings.MEDIA_ROOT, 'games', 'image', new_image_name)

            # Di chuyển ảnh tới tên mới
            with open(new_image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            # Trả lại đường dẫn mới cho ảnh
            return os.path.join('games', 'image', new_image_name)

        return image
    
    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     if file:
    #         # Lấy phần mở rộng và tên file
    #         file_name = os.path.basename(file.name)
    #         file_extension = os.path.splitext(file_name)[1].lower()

    #         # Tạo tên file mới theo công thức: {tên_game}_file_{ngẫu nhiên}
    #         new_file_name = f"{slugify(self.cleaned_data.get('name'))}_file_{uuid.uuid4().hex}{file_extension}"
            
    #         # Di chuyển file tới tên mới trong MEDIA_ROOT
    #         new_file_path = os.path.join(settings.MEDIA_ROOT, 'games', 'file', new_file_name)
            
    #         # Di chuyển file tới tên mới
    #         with open(new_file_path, 'wb') as f:
    #             for chunk in file.chunks():
    #                 f.write(chunk)

    #         # Trả lại đường dẫn mới cho file
    #         return os.path.join('games', 'file', new_file_name)

    #     return file