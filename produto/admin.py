from django.contrib import admin
from .models import Produto, Produto_TipoMatPrima

class ProdutoTipoMatPrimaInline(admin.TabularInline):
    model = Produto_TipoMatPrima
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ProdutoTipoMatPrimaInline]

@admin.register(Produto_TipoMatPrima)
class ProdutoTipoMatPrimaAdmin(admin.ModelAdmin):
    pass