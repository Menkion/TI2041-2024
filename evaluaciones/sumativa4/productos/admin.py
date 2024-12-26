from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, TipoCaracteristica, Marca, Categoria, CustomUser

admin.site.register(TipoCaracteristica)
admin.site.register(Marca)
admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'codigo', 'precio', 'fecha_vencimiento')
    search_fields = ('nombre', 'codigo')

# Registro del modelo CustomUser en el admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
