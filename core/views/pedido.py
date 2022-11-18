from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer, PedidoPostSerializer


class PedidoViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return PedidoPostSerializer

        return PedidoSerializer

    def get_queryset(self):
        usuario = self.request.user

        if usuario.admin:
            return Pedido.objects.all()

        return Pedido.objects.filter(usuario_dono=usuario)
