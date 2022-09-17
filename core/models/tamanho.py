from django.db import models


class Tamanho(models.Model):
    descricao = models.IntegerField()

    def __str__(self):
        return f"{self.descricao}"
