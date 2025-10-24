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

class DeliveryAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='delivery_profile')
    delivery_start_time = models.TimeField()
    delivery_end_time = models.TimeField()
    adress = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"