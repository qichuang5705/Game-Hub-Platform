from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('player', 'Player'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Player')
    is_verified = models.BooleanField(default=False)