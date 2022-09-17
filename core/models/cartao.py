from django.db import models

from core.models.usuario import Usuario


class Cartao(models.Model):
    usuario_dono = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    numero_cartao = models.CharField(max_length=16, unique=True)
    cvv = models.IntegerField()
    data_vencimento = models.CharField(max_length=5)
    bandeira = models.CharField(max_length=45)
    nome_dono = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.bandeira}, **** **** **** **{self.numero_cartao[-2::]} - {self.nome_dono}"
