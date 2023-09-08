
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)

    nome_empresa = models.CharField(max_length=50)

    is_admin = models.BooleanField(null=True, default=False)

   
