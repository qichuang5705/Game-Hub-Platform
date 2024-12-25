from django.db import models

from accounts.models import User

# Create your models here.
class DesignerPaymentInfo(models.Model):
    designer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='payment_info')
    account_details = models.TextField()