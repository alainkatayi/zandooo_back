from rest_framework import serializers
from .models import Product
from shops.serializers import ShopSerializer


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    image = serializers.ImageField(required=True, allow_null=False)
    stock = serializers.IntegerField(required=True)
    shop = ShopSerializer(read_only=True)


    class Meta:
        model = Product
        fields = ['id','name','description','image','stock','price','shop']
        read_only_fields = ['id','shop']