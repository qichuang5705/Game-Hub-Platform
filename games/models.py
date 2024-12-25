from django.db import models
from django.conf import settings 
from accounts.models import User

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')

class Leaderboard(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='leaderboard')
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField()

class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField()

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use User directly
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.game.title} by {self.user.username}"