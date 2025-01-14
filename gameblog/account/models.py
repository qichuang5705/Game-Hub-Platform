from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    role = models.CharField(null=True, max_length=255)
    avatar = models.ImageField(upload_to='image/', null=True, blank=True)
