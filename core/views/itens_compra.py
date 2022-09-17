from rest_framework.viewsets import ModelViewSet

from core.models import ItensCompra
from core.serializers import ItensCompraSerializer


class ItensCompraViewSet(ModelViewSet):
    queryset = ItensCompra.objects.all()
    serializer_class = ItensCompraSerializer
