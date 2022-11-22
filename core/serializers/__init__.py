from .avaliacao import AvaliacaoSerializer, AvaliacaoNestedSerializer
from .cartao import CartaoSerializer
from .cor import CorSerializer
from .endereco import EnderecoSerializer
from .forma_pagamento import Forma_PagamentoSerializer
from .itens_compra import (
    ItensCompraSerializer,
    ItensCompraSerializerNested,
    CriarEditarItensCompraSerializer,
)
from .marca import MarcaSerializer
from .pedido import PedidoSerializer, PedidoPostSerializer
from .produto import ProdutoSerializer
from .tamanho import TamanhoSerializer
from .usuario import UsuarioSerializer, UsuarioPostSerializer
