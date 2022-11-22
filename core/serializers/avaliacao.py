from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from core.models import Avaliacao
from core.serializers.usuario import UsuarioSerializer


class AvaliacaoSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Avaliacao
        fields = "__all__"


class AvaliacaoNestedSerializer(ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Avaliacao
        fields = (
            "usuario",
            "nota",
            "texto",
            "recomendou",
            "data_avaliacao",
        )
