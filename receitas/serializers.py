from rest_framework import serializers
from .models import Receita

class ReceitaSerializer(serializers.ModelSerializer):

      
 
   def create(self, validated_data: dict) -> Receita:
        
        return Receita.objects.create(**validated_data)
     

   
   class Meta:
        model = Receita
        fields = ["id", "nome", "valor",]
  