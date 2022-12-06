from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer, ProdutoPostSerializer

from core.paginations.produto import ProdutoPagination


class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    pagination_class = ProdutoPagination

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ProdutoSerializer
        return ProdutoPostSerializer

    def get_queryset(self):
        genero = self.request.query_params.get("genero")

        if not genero or genero == "Todos":
            return Produto.objects.all()
        else:
            return Produto.objects.filter(genero=genero)
