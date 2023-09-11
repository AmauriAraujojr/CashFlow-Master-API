from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Caixa
from.serializers import CaixaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner




class CaixaView(ListCreateAPIView):
 authentication_classes = [JWTAuthentication]
 permission_classes = [IsAuthenticated]
 
 queryset= Caixa.objects.all().order_by("id")
 serializer_class= CaixaSerializer

 def perform_create(self, serializer):

   return serializer.save(user=self.request.user)
 
 def get_queryset(self):
        return Caixa.objects.filter(user=self.request.user)


class CaixaDetailView(RetrieveUpdateDestroyAPIView):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsAuthenticated, IsOwner]
   
   queryset= Caixa.objects.all()
   serializer_class= CaixaSerializer