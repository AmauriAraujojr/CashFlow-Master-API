from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
     token = super().get_token(user)
     token["user_username"] = user.username
     token["user_email"] = user.email
     token["user_nome_empresa"] = user.nome_empresa
     token["user_avatar_empresa"] = user.avatar_empresa



     return token

class UserSerializer(serializers.ModelSerializer):
  
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True)


    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    

    class Meta:
        model = User
        fields = ["id", "username", "password", "email","nome_empresa","avatar_empresa"]


 
