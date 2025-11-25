from rest_framework import serializers
from .models import Shop
from accounts.serializers import UserSerializer

class ShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    opening_hours = serializers.TimeField(required=True)
    closing_hours = serializers.TimeField(required=True)
    adress = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)
    logo = serializers.ImageField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'description', 'opening_hours', 'closing_hours', 'adress', 'owner', 'logo','created_at']
        read_only_fields = ['id', 'owner', 'created_at']