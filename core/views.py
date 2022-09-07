from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.serializers import EnderecoSerializer, CartaoSerializer, CorSerializer, TamanhoSerializer, MarcaSerializer, Forma_PagamentoSerializer, PedidoSerializer, AvaliacaoSerializer
from core.models import Endereco, Cartao, Cor, Tamanho, Marca, Forma_Pagamento, Pedido, Avaliacao


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class TamanhoViewSet(ModelViewSet):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class Forma_PagamentoViewSet(ModelViewSet):
    queryset = Forma_Pagamento.objects.all()
    serializer_class = Forma_PagamentoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
