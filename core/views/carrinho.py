from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer


class CarrinhoViewSet(ModelViewSet):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Pedido.objects.filter(finalizado=False, usuario_dono=usuario)
