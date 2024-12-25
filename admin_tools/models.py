from django.db import models

from accounts.models import User

# Create your models here.
class AdminLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_logs')
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)