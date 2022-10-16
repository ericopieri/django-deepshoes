from rest_framework.viewsets import ModelViewSet

from core.models import Endereco
from core.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Endereco.objects.filter(usuario=usuario)
