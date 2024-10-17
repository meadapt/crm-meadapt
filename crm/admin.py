from django.contrib import admin
from .models import Venda, Loja, Vendedor, Produto, Cliente

# Register your models here.

class VendaAdmin(admin.ModelAdmin):
    pass

class LojaAdmin(admin.ModelAdmin):
    pass

class VendedorAdmin(admin.ModelAdmin):
    pass

class ProdutoAdmin(admin.ModelAdmin):
    pass

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venda, VendaAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)