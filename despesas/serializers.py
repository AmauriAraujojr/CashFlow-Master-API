from rest_framework import serializers
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):

      
 
   def create(self, validated_data: dict) -> Despesa:
        
        return Despesa.objects.create(**validated_data)
     

   
   class Meta:
        model = Despesa
        fields = ["id", "nome", "valor",]
  