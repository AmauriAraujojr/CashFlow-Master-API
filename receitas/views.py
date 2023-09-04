from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Receita
from .serializers import ReceitaSerializer
from django.shortcuts import get_object_or_404
from caixas.models import Caixa



class ReceitasView(CreateAPIView):

    queryset= Receita.objects.all()
    serializer_class= ReceitaSerializer
    

    def perform_create(self, serializer):
            caixa_id=self.kwargs.get("pk")
            caixa = get_object_or_404(Caixa, id=caixa_id)

            return serializer.save(caixa=caixa)
    
class ReceitasAllView(ListAPIView):
    queryset= Receita.objects.all()
    serializer_class= ReceitaSerializer

class ReceitasDetailView(RetrieveUpdateDestroyAPIView):
     queryset= Receita.objects.all()
     serializer_class= ReceitaSerializer
    