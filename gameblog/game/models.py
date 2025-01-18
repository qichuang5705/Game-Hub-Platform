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
    file = models.FileField(upload_to='games', null=True, blank=True)
    game_type = models.CharField(
        max_length=50,
        choices=[('html5', 'HTML5'), ('unity-webgl', 'Unity WebGL')],
        default='html5'
    )
    def get_file_url(self):
        if self.file:
            return self.file.url  # URL truy cập file đã upload
        return None
class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    words = RichTextField()