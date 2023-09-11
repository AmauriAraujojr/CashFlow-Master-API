from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
  
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(write_only=True)


    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    

    class Meta:
        model = User
        fields = ["id", "username", "password", "email","nome_empresa",]

 
