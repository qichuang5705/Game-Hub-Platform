from django.db import models
from account.models import User

# Create your models here.



class Game(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)

class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    words = models.TextField()