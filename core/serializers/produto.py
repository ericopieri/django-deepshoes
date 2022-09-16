from rest_framework.serializers import ModelSerializer, CharField

from core.models import Produto


class ProdutoSerializer(ModelSerializer):
    cor = CharField(source="cor.descricao")
    tamanho = CharField(source="tamanho.descricao")
    marca = CharField(source="marca.descricao")

    class Meta:
        model = Produto
        fields = "__all__"
