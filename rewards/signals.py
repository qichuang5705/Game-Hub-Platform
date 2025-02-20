from django.contrib.auth.signals import user_logged_out
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import CustomUser, FrameAvatar, FrameChat
import datetime
from django.contrib import messages


@receiver(user_logged_out)
def update_online_time(sender, request, user, **kwargs):   
    if user.is_authenticated:
        last_login = user.last_login
        logout_time = now()  
        session_duration = logout_time - last_login  

        user.total_online_time += session_duration
        user.save()

        minutes_online = user.total_online_time.total_seconds() / 60
        diem = int(minutes_online / 1)
        diemnhan = diem - user.points

        messages.success(request, f"🎉 Bạn đã đạt {diemnhan} điểm thưởng!")

        user.points = diem
        user.save()


@receiver(post_delete, sender=FrameChat)
def delete_image_file(sender, instance, **kwargs):
    """Tự động xóa ảnh khi object bị xóa"""
    if instance.image:
        instance.image.delete(save=False)  # Xóa file ảnh của khung chat


@receiver(post_delete, sender=FrameAvatar)
def delete_image_file(sender, instance, **kwargs):
    """Tự động xóa ảnh khi object bị xóa"""
    if instance.image:
        instance.image.delete(save=False)  # Xóa file ảnh của khung avatar