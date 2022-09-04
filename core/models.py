from django.db import models

from datetime import datetime


class Tipo_Usuario(models.Model):
    descricao = models.CharField(max_length=45, unique=True)


class Usuario(models.Model):
    id_tipousuario_FK = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT)
    email = models.EmailField(max_length=120)
    senha = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=10, default="Indefinido")
    contato = models.CharField(max_length=15, null=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField(default=datetime.now)


class Endereco(models.Model):
    id_usuario_FK = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    estado = models.CharField(max_length=2)
    municipio = models.CharField(max_length=75)
    bairro = models.CharField(max_length=75)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    referencia = models.CharField(255, null=True)