from django.urls import path
from .views import lista_productos, registrar_producto, guardar_producto, resultado_view, eliminar_producto, resultado_producto

urlpatterns = [
    path('', lista_productos, name='listar_productos'),
    path('registro/', registrar_producto, name='registrar_producto'),
    path('guardar/', guardar_producto, name='guardar_producto'),
    path('resultado/', resultado_view, name='resultado_view'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('productos/resultado/<int:producto_id>/', resultado_view, name='resultado_producto'),  # URL para la vista de resultado


]