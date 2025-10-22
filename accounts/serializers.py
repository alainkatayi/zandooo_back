from rest_framework import serializers
from .models import User,DeliveryAgent

class DeliveryAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgent
        fields = ['adress', 'delivery_start_time', 'delivery_end_time', 'phone_number']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    delivery_Agent_Profile = DeliveryAgentSerializer(required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password','role','delivery_Agent_Profile']

    def create(self, validated_data):
        role = validated_data.pop('role', None)
        delivery_agent_data = validated_data.pop('delivery_Agent_Profile', None)
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if role == 'delivery' and delivery_agent_data:
            DeliveryAgent.objects.create(user=user, **delivery_agent_data)


        if role:
            user.role = role
            user.save()
        return user