from django.db import models
from caixas.models import Caixa

class ReceitaChoices(models.TextChoices):
    DINHEIRO = "dinheiro",
    CARTAO= "cartao",
    PIX = "pix"


class Receita(models.Model):
    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits = 7, decimal_places = 2)
    tipo = models.CharField(max_length=100, choices=ReceitaChoices.choices, default=ReceitaChoices.DINHEIRO)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE, related_name="receitas")

    