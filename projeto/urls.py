from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import (
    UsuarioViewSet,
    EnderecoViewSet,
    CartaoViewSet,
    CorViewSet,
    TamanhoViewSet,
    MarcaViewSet,
    Forma_PagamentoViewSet,
    ProdutoViewSet,
    Ped_ProViewSet,
    PedidoViewSet,
    AvaliacaoViewSet
)

router = DefaultRouter()
router.register(r"api/usuarios", UsuarioViewSet)
router.register(r"api/enderecos", EnderecoViewSet)
router.register(r"api/cartoes", CartaoViewSet)
router.register(r"api/cores", CorViewSet)
router.register(r"api/forma_pagamento", Forma_PagamentoViewSet)
router.register(r"api/marcas", MarcaViewSet)
router.register(r"api/tamanhos", TamanhoViewSet)
router.register(r"api/produtos", ProdutoViewSet)
router.register(r"api/itens_pedido", Ped_ProViewSet)
router.register(r"api/pedidos", PedidoViewSet)
router.register(r"api/avaliacoes", AvaliacaoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
