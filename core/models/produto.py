from django.db import models

from core.models.cor import Cor
from core.models.tamanho import Tamanho
from core.models.marca import Marca


class Produto(models.Model):
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nome = models.CharField(max_length=75)
    descricao = models.TextField()
    genero = models.CharField(max_length=10, default="Indefinido")
    qtd_estoque = models.IntegerField()
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="produtos")
    tamanho = models.ForeignKey(
        Tamanho, on_delete=models.PROTECT, related_name="produtos"
    )
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="produtos")
    imagem = models.ImageField()

    def __str__(self):
        return f"{self.nome} - {self.genero}, {self.marca}, {self.cor}, {self.tamanho}"
