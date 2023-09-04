from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Despesa
from .serializers import DespesaSerializer
from django.shortcuts import get_object_or_404
from caixas.models import Caixa


class DespesaView(CreateAPIView):

    queryset=Despesa.objects.all()
    serializer_class= DespesaSerializer
    

    def perform_create(self, serializer):
            caixa_id=self.kwargs.get("pk")
            caixa = get_object_or_404(Caixa, id=caixa_id)

            return serializer.save(caixa=caixa)

class DespesasAllView(ListAPIView):
      
    queryset=Despesa.objects.all()
    serializer_class= DespesaSerializer

class DespesasDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Despesa.objects.all()
    serializer_class= DespesaSerializer