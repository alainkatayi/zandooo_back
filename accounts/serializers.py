from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password','role']

    def create(self, validated_data):
        role = validated_data.pop('role', None)
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if role:
            user.role = validated_data['role']
            user.save()
        return user