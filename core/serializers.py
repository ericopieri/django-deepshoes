from dataclasses import field
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from core.models import (
    Usuario,
    Endereco,
    Cartao,
    Cor,
    Tamanho,
    Marca,
    Produto,
    Pedido,
    Avaliacao,
    Forma_Pagamento,
    ItensCompra,
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = "__all__"


class Forma_PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forma_Pagamento
        fields = "__all__"


class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"


class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    cor = serializers.CharField(source="cor.descricao")
    tamanho = serializers.CharField(source="tamanho.descricao")
    marca = serializers.CharField(source="marca.descricao")

    class Meta:
        model = Produto
        fields = "__all__"


class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1


class ItensCompraSerializerNested(serializers.ModelSerializer):
    sub_total = serializers.SerializerMethodField()
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


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItensCompraSerializerNested(many=True)
    forma_pagamento = serializers.CharField(source="forma_pagamento.descricao")

    class Meta:
        model = Pedido
        fields = "__all__"
        depth = 1


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
