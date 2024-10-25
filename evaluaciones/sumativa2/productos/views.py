from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Marca, Caracteristica
from .forms import ProductoForm, CaracteristicaForm
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.core.exceptions import ValidationError

def resultado_view(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  # Obtener el producto por ID
    return render(request, 'productos/resultado.html', {'producto': producto})  # Pasar el producto a la plantilla

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == "POST":
        producto.delete()
        return redirect('listar_productos') 
    
def registrar_producto(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        caracteristica_form = CaracteristicaForm(request.POST)

        if producto_form.is_valid() and caracteristica_form.is_valid():
            producto = producto_form.save(commit=False)
            categoria_id = request.POST.get('categoria')
            producto.categoria = Categoria.objects.get(id=categoria_id)
            producto.save()

            # Guardar las características
            caracteristicas_data = request.POST.getlist('caracteristicas')  # Asegúrate de que esto sea correcto
            for caracteristica_data in caracteristicas_data:
                caracteristica = Caracteristica(producto=producto, **caracteristica_data)
                caracteristica.save()

            return redirect('resultado_producto', producto_id=producto.id)
    
    else:
        producto_form = ProductoForm()
        caracteristica_form = CaracteristicaForm()

    return render(request, 'productos/registro.html', {
        'producto_form': producto_form,
        'caracteristica_form': caracteristica_form,
        'categorias': categorias,
    })

def guardar_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        caracteristica_form = CaracteristicaForm(request.POST)

        if producto_form.is_valid() and caracteristica_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.caracteristica = caracteristica_form.cleaned_data['caracteristica']  # Guarda el texto de la característica
            producto.save()
            return redirect('resultado_producto', producto_id=producto.id)
    
    else:
        producto_form = ProductoForm()
        caracteristica_form = CaracteristicaForm()

    return render(request, 'productos/registro.html', {
        'producto_form': producto_form,
        'caracteristica_form': caracteristica_form,
    })

def resultado_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        return render(request, 'productos/resultado.html', {'producto': producto})
    except Producto.DoesNotExist:
        return render(request, 'productos/resultado.html', {'error': 'Producto no encontrado.'})

def test_template(request):
    try:
        get_template('productos/consulta.html')
        return HttpResponse("Plantilla encontrada.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

def filtrar_productos(request):
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
