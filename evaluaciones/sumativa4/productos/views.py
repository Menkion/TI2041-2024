from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.template.loader import get_template
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Categoria, Marca, Caracteristica
from .forms import ProductoForm, CaracteristicaForm
from .serializers import ProductoSerializer, CategoriaSerializer, MarcaSerializer
from datetime import datetime
from .forms import CustomUserCreationForm
from django import forms
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, schema
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    operation_description="Obtener la lista de productos",
    responses={200: ProductoSerializer(many=True)}
)
@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)



class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')
    is_admin = forms.BooleanField(required=False, label='¿Es administrador?')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# === API Views ===
class ProductoDeleteAPI(APIView):
    """
    Vista para eliminar un producto.
    """
    def delete(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
            producto.delete()
            return Response({"message": "Producto eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
class ProductoListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductoCreateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Crea un nuevo producto.
        """
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoUpdateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        """
        Actualiza un producto existente.
        """
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductoSerializer(producto, data=request.data, partial=True)  # Permite actualizaciones parciales
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TokenObtain(TokenObtainPairView):
    pass

def lista_productos(request):
    """
    Muestra una lista de todos los productos.
    """
    productos = Producto.objects.all()
    return render(request, 'productos/consulta_productos.html', {'productos': productos})

def consulta_productos(request):
    # Lógica para mostrar productos
    return render(request, 'productos/consulta_productos.html')

def registrar_producto(request):
    """
    Maneja el formulario de registro de un producto.
    """
    categorias = Categoria.objects.all()
    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto = producto_form.save()
            return redirect('resultado_producto', producto_id=producto.id)
    else:
        producto_form = ProductoForm()

    return render(request, 'productos/registro.html', {
        'producto_form': producto_form,
        'categorias': categorias,
    })


def eliminar_producto(request, producto_id):
    """
    Elimina un producto existente.
    """
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})



def resultado_producto(request, producto_id):
    """
    Muestra los detalles de un producto específico.
    """
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/resultado.html', {'producto': producto})


def filtrar_productos(request):
    """
    Filtra productos por categoría, marca o característica.
    """
    categoria_id = request.GET.get('categoria')
    marca_id = request.GET.get('marca')
    caracteristica_id = request.GET.get('caracteristica')

    productos = Producto.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if caracteristica_id:
        productos = productos.filter(caracteristicas__id=caracteristica_id)

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    caracteristicas = Caracteristica.objects.all()

    return render(request, 'productos/filtrar_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'marcas': marcas,
        'caracteristicas': caracteristicas,
    })


def test_template(request):
    try:
        get_template('productos/consulta.html')  # Intenta cargar la plantilla
        return HttpResponse("Plantilla encontrada.")  # Si la plantilla se carga, responde con éxito
    except Exception as e:
        return HttpResponse(f"Error: {e}")


# Vista para crear un producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

def login_view(request):
    """
    Vista para manejar el inicio de sesión.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirige al dashboard de admin si es superusuario
            else:
                return redirect('listar_productos')  # Redirige a la lista de productos
        else:
            messages.error(request, 'Credenciales incorrectas. Intenta de nuevo.')
    
    return render(request, 'productos/login.html')

def logout_view(request):
    """
    Cierra la sesión del usuario y redirige a la página de inicio de sesión.
    """
    logout(request)
    return redirect('productos/login.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')  # Redirige a la página de tu elección
    else:
        form = CustomUserCreationForm()
    return render(request, 'crear_usuario.html', {'form': form})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    """
    Vista del panel de opciones para el administrador.
    """
    return render(request, 'productos/admin_dashboard.html')