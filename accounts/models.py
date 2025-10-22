from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role_choice = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('delivery', 'Delivery'),
    ]
    role = models.CharField(
        max_length=20,
        choices=role_choice,
        default='user'
    )
    def __str__(self):
        return self.email