from django.db import models
from abstracts_models.soft_delete_model import SoftDeleteModel
from manager.soft_delete_manager import SoftDeleteManager
from shops.models import Shop
from abstracts_models.time_stamped_model import TimeStampedModel

# Create your models here.
class Product(TimeStampedModel,SoftDeleteModel):
    objects = SoftDeleteManager()

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products_images/', null=False)
    stock = models.IntegerField()
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='store')