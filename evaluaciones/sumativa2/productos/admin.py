from django.contrib import admin
from .models import Producto, TipoCaracteristica, Marca, Categoria

# Solo mostramos el modelo de tipos de características en el administrador.
admin.site.register(TipoCaracteristica)
admin.site.register(Marca)
admin.site.register(Categoria)

# Si deseas gestionar productos, puedes agregar también el modelo de Producto:
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'precio', 'fecha_vencimiento')
