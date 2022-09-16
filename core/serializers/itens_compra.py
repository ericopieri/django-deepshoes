from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import ItensCompra
from core.serializers.produto import ProdutoSerializer


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1


class ItensCompraSerializerNested(ModelSerializer):
    sub_total = SerializerMethodField()
    produto = ProdutoSerializer()

    class Meta:
        model = ItensCompra
        fields = (
            "produto",
            "qtd_produto",
            "sub_total",
            "data_entrada",
        )
        depth = 1

    def get_sub_total(self, obj):
        return obj.qtd_produto * obj.produto.valor_unitario
