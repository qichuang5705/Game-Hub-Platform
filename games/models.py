from django.db import models
from accounts.models import CustomUser
import os
import zipfile
from accounts.models import CustomUser
# Create your models here.



class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    file = models.FileField(upload_to='games/', null=True, blank=True)
    version = models.TextField(max_length=15, default=1.0)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        if self.file:  # Kiểm tra nếu file được upload
            file_path = self.file.path
            if zipfile.is_zipfile(file_path):  # Kiểm tra nếu file là .zip
                # Tạo thư mục cùng cấp để lưu nội dung giải nén
                extract_dir = os.path.splitext(file_path)[0]  # Thư mục có tên giống file (bỏ đuôi .zip)

                if not os.path.exists(extract_dir):  # Tạo thư mục nếu chưa tồn tại
                    os.makedirs(extract_dir)

                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)  # Giải nén vào thư mục

                # (Tùy chọn) Xóa file .zip sau khi giải nén
                os.remove(file_path)

                # Xóa tham chiếu đến file zip
                self.file = None
                super().save(*args, **kwargs)  # Lưu lại để cập nhật database

class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    words = models.TextField()