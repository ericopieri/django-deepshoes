from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

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
router.register(r"usuarios", UsuarioViewSet, basename="usuarios")
router.register(r"enderecos", EnderecoViewSet, basename="enderecos")
router.register(r"cartoes", CartaoViewSet)
router.register(r"cores", CorViewSet)
router.register(r"forma_pagamento", Forma_PagamentoViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"tamanhos", TamanhoViewSet)
router.register(r"produtos", ProdutoViewSet, basename="produtos")
router.register(r"itens_pedido", ItensCompraViewSet)
router.register(r"pedidos", PedidoViewSet, basename="pedidos")
router.register(r"avaliacoes", AvaliacaoViewSet)
router.register(r"carrinho", CarrinhoViewSet, basename="carrinho")


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
]
