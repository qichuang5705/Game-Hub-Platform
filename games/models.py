from django.db import models
from accounts.models import CustomUser

# Create your models here.



class Game(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    file = models.FileField(upload_to='games/', null=True, blank=True)
    game_type = models.CharField(
        max_length=50,
        choices=[('html5', 'HTML5'), ('unity-webgl', 'Unity WebGL')],
        default='html5'
    )

class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    words = models.TextField()