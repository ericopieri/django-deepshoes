from rest_framework.viewsets import ModelViewSet

from core.models import Avaliacao
from core.serializers import AvaliacaoSerializer, AvaliacaoNestedSerializer
from core.paginations.avaliacao import AvaliacaoPagination


class AvaliacaoViewSet(ModelViewSet):
    pagination_class = AvaliacaoPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AvaliacaoNestedSerializer

        return AvaliacaoSerializer

    def get_queryset(self):
        id = self.request.query_params.get("id")

        return Avaliacao.objects.filter(id=id).order_by("data_avaliacao")
