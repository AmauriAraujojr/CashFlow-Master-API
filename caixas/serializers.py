from rest_framework import serializers
from .models import Caixa
from receitas.serializers import ReceitaSerializer
from despesas.serializers import DespesaSerializer

class CaixaSerializer(serializers.ModelSerializer):

      
   receitas = ReceitaSerializer(read_only=True, many=True)
   despesas =DespesaSerializer(read_only=True, many=True)

   def create(self, validated_data: dict) -> Caixa:
        
        return Caixa.objects.create(**validated_data)
     
   class Meta:
        model = Caixa
        fields = ["id", "data", "despesas", "receitas"]
  