from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import Usuario
from core.serializers import UsuarioSerializer, UsuarioPostSerializer


class UsuarioViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        usuario = self.request.user

        return Usuario.objects.filter(email=usuario.email)

    def get_serializer_class(self):
        if self.action == "create":
            return UsuarioPostSerializer

        return UsuarioSerializer
