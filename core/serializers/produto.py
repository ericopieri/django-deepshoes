from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
    ValidationError,
)
from drf_extra_fields.fields import Base64ImageField

from core.models import Produto, Avaliacao
from core.serializers import AvaliacaoNestedSerializer


class ProdutoSerializer(ModelSerializer):
    cor = CharField(source="cor.descricao")
    tamanho = CharField(source="tamanho.descricao")
    marca = CharField(source="marca.descricao")
    porcentagem_recomendado = SerializerMethodField()

    class Meta:
        model = Produto
        fields = "__all__"

    def get_porcentagem_recomendado(self, instance):
        porcentagem_recomendado = Avaliacao.objects.filter(
            produto=instance, recomendou=True
        ).count()
        porcentagem_geral = Avaliacao.objects.filter(produto=instance).count()

        if porcentagem_geral > 0:
            return round((porcentagem_recomendado / porcentagem_geral) * 100, 2)

        return 0


class ProdutoPostSerializer(ModelSerializer):
    imagem = Base64ImageField()

    class Meta:
        model = Produto
        fields = (
            "id",
            "cor",
            "marca",
            "tamanho",
            "valor_unitario",
            "nome",
            "descricao",
            "genero",
            "qtd_estoque",
            "imagem",
        )

    def create(self, validated_data):
        permissao = self.context.get("request").user.admin

        if permissao:
            produto = Produto.objects.create(**validated_data)
            return produto
        else:
            raise ValidationError(
                {
                    "permissao": "Você não tem o nível de permissão para cadastrar um produto!"
                }
            )
