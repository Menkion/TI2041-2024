from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from productos.views import (
    login_view, lista_productos, registrar_producto, crear_producto, resultado_producto,
    eliminar_producto, ProductoListAPI, ProductoCreateAPI, ProductoUpdateAPI, ProductoDeleteAPI
)


schema_view = get_schema_view( 
    openapi.Info( 
        title="API de Gestión de Productos", 
        default_version='v1', 
        description="Documentación de la API para la gestión de productos", 
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(email="contacto@tudominio.com"), 
        license=openapi.License(name="BSD License"), 
        ), 
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de la aplicación 'productos'
    path('', lista_productos, name='listar_productos'),
    path('registro/', registrar_producto, name='registrar_producto'),
    path('guardar/', crear_producto, name='guardar_producto'),
    path('resultado/<int:producto_id>/', resultado_producto, name='resultado_producto'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('login/', login_view, name='login'),
    # Rutas API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/productos/', ProductoListAPI.as_view(), name='producto_list'),
    path('api/productos/create/', ProductoCreateAPI.as_view(), name='producto_create'),
    path('api/productos/<int:pk>/update/', ProductoUpdateAPI.as_view(), name='producto_update'),
    path('api/productos/<int:pk>/delete/', ProductoDeleteAPI.as_view(), name='producto_delete'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('consulta_productos/', views.consulta_productos, name='consulta_productos'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
