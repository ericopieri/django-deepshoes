from django.db import models


class Forma_Pagamento(models.Model):
    descricao = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.descricao
