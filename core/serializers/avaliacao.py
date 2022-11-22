from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from core.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Avaliacao
        fields = "__all__"
