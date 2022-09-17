from rest_framework.viewsets import ModelViewSet

from core.models import Cartao
from core.serializers import CartaoSerializer


class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
