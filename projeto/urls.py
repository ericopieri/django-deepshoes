from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    UsuarioViewSet,
    EnderecoViewSet,
    CartaoViewSet,
    CorViewSet,
    TamanhoViewSet,
    MarcaViewSet,
    Forma_PagamentoViewSet,
    ProdutoViewSet,
    ItensCompraViewSet,
    PedidoViewSet,
    AvaliacaoViewSet,
    CarrinhoViewSet,
)

router = DefaultRouter()
router.register(r"api/usuarios", UsuarioViewSet, basename="usuarios")
router.register(r"api/enderecos", EnderecoViewSet)
router.register(r"api/cartoes", CartaoViewSet)
router.register(r"api/cores", CorViewSet)
router.register(r"api/forma_pagamento", Forma_PagamentoViewSet)
router.register(r"api/marcas", MarcaViewSet)
router.register(r"api/tamanhos", TamanhoViewSet)
router.register(r"api/produtos", ProdutoViewSet, basename="produtos")
router.register(r"api/itens_pedido", ItensCompraViewSet)
router.register(r"api/pedidos", PedidoViewSet, basename="pedidos")
router.register(r"api/avaliacoes", AvaliacaoViewSet)
router.register(r"api/carrinho", CarrinhoViewSet, basename="carrinho")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
]
