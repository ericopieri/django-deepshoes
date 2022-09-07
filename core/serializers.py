from rest_framework import serializers
from core.models import Endereco, Cartao, Cor, Tamanho, Marca, Produto, Pedido, Avaliacao


class EnderecoSerializer(serializers.Serializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class CartaoSerializer(serializers.Serializer):
    class Meta:
        model = Cartao
        fields = "__all__"

    
class CorSerializer(serializers.Serializer):
    class Meta:
        model = Cor
        fields = "__all__"


class TamanhoSerializer(serializers.Serializer):
    class Meta:
        model = Tamanho
        fields = "__all__"


class MarcaSerializer(serializers.Serializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProdutoSerializer(serializers.Serializer):
    class Meta:
        model = Produto
        fields = "__all__"


class PedidoSerializer(serializers.Serializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class AvaliacaoSerializer(serializers.Serializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
