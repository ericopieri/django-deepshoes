from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils import timezone
from datetime import datetime


class UsuarioManager(BaseUserManager):
    def _create_user(
        self, email, password, admin, super_usuario, staff, **extra_fields
    ):
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
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, True, **extra_fields)
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
    staff = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["cpf", "sexo", "contato", "nome", "sobrenome", "dt_nasc"]

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
