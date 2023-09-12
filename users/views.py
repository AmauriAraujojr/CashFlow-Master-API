from .models import User
from .serializers import UserSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
