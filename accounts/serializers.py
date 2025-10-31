from rest_framework import serializers
from .models import User,DeliveryAgent
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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

#custome de la class TokenObtainPair qui renvoi par defaut seulement: access et refresh
#on ajout un objet user, pour avoir aussi les informations du user qui se connecte
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        #gestion de response en fonction du role
        

        #si le user est un delivery, on ajoute son profile de delivery dans la reponse
        if self.user.role == 'delivery':
            delivery_profile = self.user.delivery_profile
            user_data = {
                'id': self.user.id,
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'role': self.user.role,
                'delivery_Agent_Profile': {
                    'adress': delivery_profile.adress,
                    'delivery_start_time': delivery_profile.delivery_start_time,
                    'delivery_end_time': delivery_profile.delivery_end_time,
                    'phone_number': delivery_profile.phone_number,
                }
            }
            data.update({'user': user_data})
            return data
        #sinon on renvoi juste les infos de base du user
        else:
            data.update({
                'user': {
                    'id': self.user.id,
                    'username': self.user.username,
                    'email': self.user.email,
                }
            })
        return data