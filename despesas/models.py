from django.db import models
from caixas.models import Caixa


class Despesa(models.Model):
    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits = 7, decimal_places = 2)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE, related_name="despesas")

    
