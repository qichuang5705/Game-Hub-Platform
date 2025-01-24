from django.db import models
from accounts.models import CustomUser
import os
import zipfile
from accounts.models import CustomUser
from django.conf import settings

# Create your models here.



class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField('Genre')
    description = models.TextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)
    image = models.ImageField(upload_to='games/image', null=True, blank=True)
    file = models.FileField(upload_to='games/file', null=True, blank=True)
    version = models.TextField(max_length=15, default=1.0)


    def extract(self):
        curr_path = self.image.path
    # def save(self, *args, **kwargs):
    #     # if not self.image:
    #     #     self.image = 'empty.jpg'  # Đặt ảnh mặc định khi không có ảnh
    #     # Lưu game vào database trước
    #     super().save(*args, **kwargs)  

    #     # Kiểm tra nếu file zip đã được upload
    #     if self.file:
    #         file_path = self.file.path  # Đường dẫn tới file zip

    #         if zipfile.is_zipfile(file_path):  # Kiểm tra nếu file là zip
    #             # Đảm bảo giải nén vào thư mục media/games/
    #             extract_dir = os.path.join(settings.MEDIA_ROOT, 'games', os.path.splitext(self.file.name)[0])

    #             if not os.path.exists(extract_dir):  # Nếu thư mục giải nén chưa tồn tại thì tạo mới
    #                 os.makedirs(extract_dir)

    #             # Giải nén file zip vào thư mục extract_dir
    #             with zipfile.ZipFile(file_path, 'r') as zip_ref:
    #                 zip_ref.extractall(extract_dir)

    #             # (Tùy chọn) Xóa file zip sau khi giải nén
    #             os.remove(file_path)

    #             # Cập nhật lại tham chiếu đến file zip (có thể xóa tham chiếu này nếu không cần thiết nữa)
    #             self.file = None
    #             super().save(*args, **kwargs)  # Lưu lại để cập nhật database


class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    words = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    

class leader_board(models.Model):
    pass