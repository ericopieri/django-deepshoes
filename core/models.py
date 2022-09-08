from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

from django.utils import timezone
from datetime import datetime


class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password, admin, super_usuario, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        usuario = self.model(
            email=email,
            admin=admin,
            super_usuario=super_usuario,
            ativo=True,
            last_login=now,
            data_criacao=now,
            **extra_fields,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.ativo = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=10, default="Indefinido")
    contato = models.CharField(max_length=15, null=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    dt_nasc = models.DateField(default=datetime.now)
    ativo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    super_usuario = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome} <{self.email}>"

    def get_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @property
    def is_staff(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return self.super_usuario

    def has_module_perms(self, app_label):
        return self.super_usuario


class Endereco(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    estado = models.CharField(max_length=2)
    municipio = models.CharField(max_length=75)
    bairro = models.CharField(max_length=75)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    referencia = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.estado}, {self.municipio}, {self.bairro} - {self.usuario}"


class Cartao(models.Model):
    usuario_dono = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    numero_cartao = models.CharField(max_length=16, unique=True)
    cvv = models.IntegerField()
    data_vencimento = models.CharField(max_length=5)
    bandeira = models.CharField(max_length=45)
    nome_dono = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.bandeira}, **** **** **** **{self.numero_cartao[-2::]} - {self.nome_dono}"


class Cor(models.Model):
    descricao = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.descricao


class Tamanho(models.Model):
    descricao = models.IntegerField()

    def __str__(self):
        return f"{self.descricao}"


class Marca(models.Model):
    descricao = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.descricao


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

    def __str__(self):
        return f"{self.nome} - {self.genero}, {self.marca}, {self.cor}, {self.tamanho}"


class Forma_Pagamento(models.Model):
    descricao = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.descricao


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
    data_pedido = models.DateField(default=datetime.now)
    finalizado = models.BooleanField(default=False)
    qtd_parcela = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    itens = models.ManyToManyField(Produto, related_name="pedidos", through="Ped_Pro")

    def __str__(self):
        return f"{self.preco_total}"


class Ped_Pro(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, related_name="ped_pros"
    )
    pedido = models.ForeignKey(
        Pedido, on_delete=models.PROTECT, related_name="ped_pros"
    )
    qtd_produto = models.IntegerField(default=1)
    data_entrada = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.produto}, {self.qtd_estoque}"


class Avaliacao(models.Model):
    produto_avaliado = models.ForeignKey(
        Ped_Pro, on_delete=models.PROTECT, related_name="avaliacoes"
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
