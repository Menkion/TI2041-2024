from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse
from django.template.loader import get_template

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})

def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('resultado_producto', producto_id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})

def guardar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        codigo = request.POST.get('codigo')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        precio = request.POST.get('precio')
        
        try:
            producto = Producto(nombre=nombre, marca=marca, codigo=codigo, fecha_vencimiento=fecha_vencimiento, precio=precio)
            producto.save()
            return render(request, 'productos/resultado.html', {'producto': producto})
        except Exception as e:
            return render(request, 'productos/resultado.html', {'error': str(e)})
    
    return redirect('registrar_producto')

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