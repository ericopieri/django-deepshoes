from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        usuario = self.request.user

        if usuario.admin:
            return Pedido.objects.all()

        return Pedido.objects.filter(usuario=usuario)
