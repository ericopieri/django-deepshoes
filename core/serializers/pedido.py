from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    HiddenField,
    CurrentUserDefault,
)

from core.serializers.itens_compra import (
    ItensCompraSerializerNested,
    CriarEditarItensCompraSerializer,
)
from core.models import Pedido, ItensCompra, Produto


class PedidoSerializer(ModelSerializer):
    itens = ItensCompraSerializerNested(many=True)
    forma_pagamento = CharField(
        source="forma_pagamento.descricao", default="Não cadastrado"
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        depth = 1


class PedidoPostSerializer(ModelSerializer):
    usuario_dono = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)

    class Meta:
        model = Pedido
        fields = (
            "id",
            "itens",
            "usuario_dono",
            "preco_total",
        )

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        pedido = Pedido.objects.create(**validated_data)

        for item in itens:
            ItensCompra.objects.create(pedido=pedido, **item)

        pedido.save()
        return pedido

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")

        if itens is not None:
            instance.itens.all().delete()

            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)

        instance.save()

        return instance
