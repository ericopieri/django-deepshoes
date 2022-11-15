from rest_framework.serializers import ModelSerializer

from core.models import Usuario


class UsuarioPostSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            "id",
            "email",
            "nome",
            "sobrenome",
            "sexo",
            "contato",
            "dt_nasc",
        )
