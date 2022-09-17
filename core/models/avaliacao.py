from django.db import models

from django.contrib.auth import get_user_model
from core.models.itens_compra import ItensCompra

from datetime import datetime


class Avaliacao(models.Model):
    produto_avaliado = models.ForeignKey(
        ItensCompra, on_delete=models.PROTECT, related_name="avaliacoes"
    )
    usuario = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="avaliacoes"
    )
    nota = models.IntegerField()
    recomendou = models.BooleanField()
    texto = models.TextField()
    data_avaliacao = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.produto_avaliado}, {self.usuario}"
