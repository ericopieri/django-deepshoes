from rest_framework.viewsets import ModelViewSet

from core.models import Avaliacao
from core.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
