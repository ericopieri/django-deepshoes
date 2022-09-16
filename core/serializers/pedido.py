from rest_framework.serializers import ModelSerializer, CharField

from core.serializers.itens_compra import ItensCompraSerializerNested
from core.models import Pedido


class PedidoSerializer(ModelSerializer):
    itens = ItensCompraSerializerNested(many=True)
    forma_pagamento = CharField(source="forma_pagamento.descricao")

    class Meta:
        model = Pedido
        fields = "__all__"
        depth = 1
