from rest_framework.viewsets import ModelViewSet

from core.models import Endereco
from core.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
