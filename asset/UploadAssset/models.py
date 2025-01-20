from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser): 
    avata = models.ImageField(upload_to='uploads/%Y/%m')
class asset (models.Model):
    price = models.IntegerField()
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    quantifier = models.IntegerField()
    title = models.CharField(max_length= 300,null=False)
    create_date = models.DateTimeField(auto_now_add= True)
    thumnail = models.ImageField(upload_to='thumnail/%Y/%m',default=True)
    User = models.ForeignKey(user,on_delete=models.SET_NULL , null= True)