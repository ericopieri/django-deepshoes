from rest_framework.serializers import ModelSerializer

from core.models import Forma_Pagamento


class Forma_PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Forma_Pagamento
        fields = "__all__"
