from django.db import models
from accounts.models import User
from abstracts_models.time_stamped_model import TimeStampedModel
from abstracts_models.soft_delete_model import SoftDeleteModel

# Create your models here.
class Shop(TimeStampedModel,SoftDeleteModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    adress = models.CharField(max_length=255)
    owner =models.ForeignKey (User, on_delete=models.CASCADE, related_name='shops')
    logo = models.ImageField(upload_to='shop_logos/', null=True, blank=True)
    

    def __str__(self):
        return self.name