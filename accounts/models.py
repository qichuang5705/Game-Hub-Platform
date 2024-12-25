from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('guest', 'Guest'),
        ('player', 'Player'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='guest')
    verification_status = models.BooleanField(default=False)
    
    # Resolve the reverse accessor issue by adding related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.'
    )