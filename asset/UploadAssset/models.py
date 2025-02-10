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
    thumnail = models.ImageField(upload_to='thumnail/%Y/%m', default='defaults/NoneImage.png', blank=True, null=True)
    User = models.ForeignKey(user,on_delete=models.SET_NULL , null= True)

class Purchase(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    asset = models.ForeignKey(asset, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])