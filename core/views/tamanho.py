from rest_framework.viewsets import ModelViewSet

from core.models import Tamanho
from core.serializers import TamanhoSerializer


class TamanhoViewSet(ModelViewSet):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer
