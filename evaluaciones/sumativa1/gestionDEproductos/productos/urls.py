from django.urls import path
from .views import lista_productos, registrar_producto, guardar_producto

urlpatterns = [
    path('', lista_productos, name='listar_productos'),  # Asegúrate de que esto coincida
    path('registro/', registrar_producto, name='registrar_producto'),
    path('guardar/', guardar_producto, name='guardar_producto'),
]
