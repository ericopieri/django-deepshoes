from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    HiddenField,
    CurrentUserDefault,
)

from decouple import config

from core.serializers.itens_compra import (
    ItensCompraSerializerNested,
    CriarEditarItensCompraSerializer,
)
from core.models import Pedido, ItensCompra, Produto

from django.core.mail import send_mail


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
            "valor_parcela",
            "qtd_parcela",
            "finalizado",
            "preco_final",
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

        instance.finalizado = validated_data.get("finalizado", instance.finalizado)
        instance.qtd_parcela = validated_data.get("qtd_parcela", instance.qtd_parcela)
        instance.valor_parcela = validated_data.get(
            "valor_parcela", instance.valor_parcela
        )
        instance.preco_final = validated_data.get("preco_final", instance.preco_final)
        instance.endereco_entrega = validated_data.get(
            "endereco_entrega", instance.endereco_entrega
        )

        if validated_data.get("finalizado", None):
            email = self.context.get("request").user.email
            send_mail(
                "Cadastro realizado com sucesso",
                "Pedido finalizado! Obrigado pela preferência, ",
                config("EMAIL_HOST_USER"),
                email,
            )

        if itens:
            instance.itens.all().delete()

            for item in itens:
                ItensCompra.objects.create(pedido=instance, **item)

        if len(itens) == 0:
            instance.delete()

        instance.save()

        return instance
