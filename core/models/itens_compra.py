from django.db import models

from core.models.pedido import Pedido
from core.models.produto import Produto


class ItensCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="+")
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    qtd_produto = models.IntegerField(default=1)
    data_entrada = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.produto}, {self.qtd_produto}"
