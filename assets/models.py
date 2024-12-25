from django.db import models

from accounts.models import User

# Create your models here.
class GameAsset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    designer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assets')
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file = models.FileField(upload_to='game_assets/')