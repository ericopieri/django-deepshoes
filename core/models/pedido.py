from django.db import models

from django.contrib.auth import get_user_model
from core.models.endereco import Endereco
from core.models.forma_pagamento import Forma_Pagamento

from datetime import date


class Pedido(models.Model):
    endereco_entrega = models.ForeignKey(
        Endereco, on_delete=models.PROTECT, null=True, related_name="pedidos"
    )
    forma_pagamento = models.ForeignKey(
        Forma_Pagamento, on_delete=models.PROTECT, null=True, related_name="pedidos"
    )
    usuario_dono = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="pedidos"
    )
    data_entrega = models.DateField()
    data_pedido = models.DateField(default=date.today)
    finalizado = models.BooleanField(default=False)
    qtd_parcela = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.preco_total} - {self.data_pedido} - {self.usuario_dono}"
