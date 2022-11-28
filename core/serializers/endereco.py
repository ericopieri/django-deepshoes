from rest_framework.serializers import ModelSerializer

from core.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            "estado",
            "municipio",
            "bairro",
            "logradouro",
            "numero",
            "complemento",
            "referencia",
            "id",
        )

    def create(self, validated_data):
        usuario = self.context["request"].user
        endereco = Endereco(**validated_data, usuario=usuario)
        endereco.save()
        return endereco
