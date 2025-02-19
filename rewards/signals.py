from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now
from .models import CustomUser
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
