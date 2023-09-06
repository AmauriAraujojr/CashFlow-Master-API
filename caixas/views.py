from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Caixa
from.serializers import CaixaSerializer


class CaixaView(ListCreateAPIView):
 
 queryset= Caixa.objects.all().order_by("id")
 serializer_class= CaixaSerializer

class CaixaDetailView(RetrieveUpdateDestroyAPIView):
  
  queryset= Caixa.objects.all()
  serializer_class= CaixaSerializer