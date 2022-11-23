from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer, PedidoPostSerializer


class PedidoViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PedidoSerializer

        return PedidoPostSerializer

    def get_queryset(self):
        concluidos = self.request.query_params.get("concluidos")

        usuario = self.request.user

        if usuario.admin:
            return Pedido.objects.all()

        if concluidos:
            return Pedido.objects.filter(usuario_dono=usuario, finalizado=True)

        return Pedido.objects.filter(usuario_dono=usuario)
