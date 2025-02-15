from django.db import models

# Create your models here.


class Reward(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tên phần thưởng
    description = models.TextField(blank=True)  # Mô tả phần thưởng
    price = models.IntegerField()  # Số điểm cần để đổi
    css_class = models.CharField(max_length=100, blank=True, null=True)  # Lớp CSS tùy chỉnh (nếu có)
    image = models.ImageField(upload_to='rewards/', blank=True, null=True)  # Ảnh hiển thị
    type = models.CharField(
        max_length=50,
        choices=[('avatar_frame', 'Khung Avatar'), ('chat_frame', 'Khung Chat'), ('effect', 'Hiệu Ứng')],
        default='effect'
    )  # Loại phần thưởng

    def __str__(self):
        return f"{self.name} ({self.price} points)"