from django.contrib import admin

from core.models import (
    Usuario,
    Endereco,
    Cartao,
    Cor,
    Tamanho,
    Marca,
    Produto,
    Forma_Pagamento,
    Pedido,
    Ped_Pro,
    Avaliacao,
)


admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Cartao)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Forma_Pagamento)
admin.site.register(Avaliacao)


class ItensInline(admin.StackedInline):
    model = Ped_Pro


@admin.register(Pedido)
class PedProInline(admin.ModelAdmin):
    inlines = (ItensInline,)
