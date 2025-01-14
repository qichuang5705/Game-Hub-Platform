from django.db import models
from account.models import User
# from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
# Create your models here.



class Game(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = RichTextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/', null=True, blank=True)

class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    words = RichTextField()