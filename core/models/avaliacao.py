from django.db import models

from core.models.itens_compra import Produto
from core.models.usuario import Usuario

from datetime import datetime


class Avaliacao(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, related_name="avaliacoes"
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="avaliacoes"
    )
    nota = models.IntegerField()
    recomendou = models.BooleanField()
    texto = models.TextField()
    data_avaliacao = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.produto_avaliado}, {self.usuario}"
