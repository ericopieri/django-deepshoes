from django.db import models

from core.models.usuario import Usuario


class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    estado = models.CharField(max_length=2)
    municipio = models.CharField(max_length=75)
    bairro = models.CharField(max_length=75)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    referencia = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.estado}, {self.municipio}, {self.bairro}, {self.logradouro}, {self.numero} - {self.usuario}"
