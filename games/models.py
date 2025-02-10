from django.db import models
from accounts.models import CustomUser
import os
import zipfile
from accounts.models import CustomUser
from django.conf import settings
import random, uuid
# Create your models here.



class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField('Genre')
    description = models.TextField()
    datecreate = models.DateField(auto_now_add=True)
    reward = models.IntegerField(default=0)
    image = models.ImageField(upload_to='games/image', null=True, blank=True)
    file = models.FileField(upload_to='games/file', null=True, blank=True)
    version = models.TextField(max_length=15, default=1.0)
    
    def extract(self):
        file_zip_path = self.file.path 
        name = os.path.basename(file_zip_path)
        name = name[0:len(name)-4]  #lấy tên file
        parent_file = os.path.dirname(file_zip_path)  #lấy file cha
        with zipfile.ZipFile(file_zip_path, 'r') as zip_ref:
            zip_ref.extractall(parent_file)
        os.remove(file_zip_path)
        new_path = os.path.join(parent_file, name)
        new_file_name = f"file_{uuid.uuid4().hex}"
        os.rename(new_path, f"{parent_file}\\{new_file_name}")
        
        url = str(self.file)
        print(url)
        new_url = f"{os.path.dirname(url)}/{new_file_name}/index.html"
        self.file = new_url
        super().save()


        



class Comment(models.Model):
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    words = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    



class LBHistory(models.Model):  #Leader board history:Lịch sử điểm của từng người chơi
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now=True)


