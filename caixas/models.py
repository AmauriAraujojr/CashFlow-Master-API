from django.db import models

class Caixa(models.Model):
   data = models.DateField(auto_now_add=True)
   total= models. DecimalField(max_digits = 8, decimal_places = 2, null= True, default=None)
   saldo_anterior= models. DecimalField(max_digits = 8, decimal_places = 2, null= True, default=None)
   user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="caixas",
    )