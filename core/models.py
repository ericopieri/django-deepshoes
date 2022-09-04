from django.db import models

from datetime import datetime


class Tipo_Usuario(models.Model):
    descricao = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.descricao


class Usuario(models.Model):
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT)
    email = models.EmailField(max_length=120)
    senha = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=10, default="Indefinido")
    contato = models.CharField(max_length=15, null=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} <{self.email}>"


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
        return f"{self.estado}, {self.municipio}"


class Cartao(models.Model):
    usuario_dono = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    numero_cartao = models.CharField(max_length=16, unique=True)
    cvv = models.IntegerField()
    data_vencimento = models.CharField(max_length=5)
    bandeira = models.CharField(max_length=45)
    nome_dono = models.CharField(max_length=120)


class Cor(models.Model):
    descricao = models.CharField(max_length=45, unique=True)


class Tamanho(models.Model):
    descricao = models.IntegerField()


class Marca(models.Model):
    descricao = models.CharField(max_length=45, unique=True)


class Produto(models.Model):
    preco = field_name = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nome = models.CharField(max_length=75)
    descricao = models.TextField()
    genero = models.CharField(max_length=10, default="Indefinido")
    qtd_estoque = models.IntegerField()
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)


class Forma_Pagamento(models.Model):
    descricao = models.CharField(max_length=45, unique=True)


class Pedido(models.Model):
    endereco_entrega = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    forma_pagamento = models.ForeignKey(Forma_Pagamento, on_delete=models.PROTECT, null=True)
    usuario_dono = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    data_entrega = models.DateField()
    data_pedido = models.DateField(default=datetime.now)
    finalizado = BooleanField(default=False)
    qtd_parcela = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    itens = models.ManyToManyField(Produto, related_name="pedidos_associados", through="Itens_Pedido")


class Itens_Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    qtd_produto = models.IntegerField(default=1)
    data_entrada = models.DateTimeField(default=datetime.now)


class Avaliacao(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nota = models.IntegerField()
    recomendou = models.BooleanField()
    texto = models.TextField()
    data_avaliacao = models.DateTimeField(default=datetime.now)
