from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from core.models import Produto, Avaliacao
from core.serializers import AvaliacaoNestedSerializer


class ProdutoSerializer(ModelSerializer):
    cor = CharField(source="cor.descricao")
    tamanho = CharField(source="tamanho.descricao")
    marca = CharField(source="marca.descricao")
    porcentagem_recomendado = SerializerMethodField()
    avaliacoes = AvaliacaoNestedSerializer(many=True)

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
