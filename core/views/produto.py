from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer

from core.paginations.produto import ProdutoPagination


class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    pagination_class = ProdutoPagination

    def get_query_set(self):
        sexo = self.request.query_params.get("sexo")

        if sexo is None:
            return Produto.objects.filter(sexo=sexo)
        else:
            return Produto.objects.all()
