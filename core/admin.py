from django.contrib import admin

from core.models import Tipo_Usuario, Usuario, Endereco, Cartao, Cor, Tamanho, Marca, Produto, Forma_Pagamento, Pedido, Itens_Pedido, Avaliacao


admin.site.register(Tipo_Usuario)
admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Cartao)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Forma_Pagamento)
admin.site.register(Pedido)
admin.site.register(Itens_Pedido)
admin.site.register(Avaliacao)

