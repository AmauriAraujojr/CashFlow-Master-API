from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Caixa
from.serializers import CaixaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from users.models import User
from django.shortcuts import get_object_or_404

 
class CaixaView(ListCreateAPIView):

 
 queryset= Caixa.objects.all().order_by("id")
 serializer_class= CaixaSerializer


 def perform_create(self, serializer):
  user_id=self.kwargs.get("pk")
  user = get_object_or_404(User, id=user_id)

  return serializer.save(user=user)
 
 def get_queryset(self):
        user_id=self.kwargs.get("pk")

        return Caixa.objects.filter(user= user_id).order_by("id")



class CaixaDetailView(RetrieveUpdateDestroyAPIView):
 
   
   queryset= Caixa.objects.all()
   serializer_class= CaixaSerializer
  