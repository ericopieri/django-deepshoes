from rest_framework.viewsets import ModelViewSet

from core.models import Forma_Pagamento
from core.serializers import Forma_PagamentoSerializer


class Forma_PagamentoViewSet(ModelViewSet):
    queryset = Forma_Pagamento.objects.all()
    serializer_class = Forma_PagamentoSerializer
