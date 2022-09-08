from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import (
    EnderecoViewSet,
    CartaoViewSet,
    CorViewSet,
    TamanhoViewSet,
    MarcaViewSet,
    Forma_PagamentoViewSet,
    PedidoViewSet,
    AvaliacaoViewSet,
    UsuarioViewSet,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"enderecos", EnderecoViewSet)
router.register(r"cartoes", CartaoViewSet)
router.register(r"cores", CorViewSet)
router.register(r"forma_pagamento", Forma_PagamentoViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"tamanhos", TamanhoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"avaliacoes", AvaliacaoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
