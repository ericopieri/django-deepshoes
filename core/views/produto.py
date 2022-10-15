from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer

from core.paginations.produto import ProdutoPagination


class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    pagination_class = ProdutoPagination

    def get_queryset(self):
        genero = self.request.query_params.get("genero")

        if genero != "Todos":
            return Produto.objects.filter(genero=genero)
        else:
            return Produto.objects.all()
