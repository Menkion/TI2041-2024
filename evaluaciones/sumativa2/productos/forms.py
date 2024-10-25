from django import forms
from .models import Producto, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'categoria', 'codigo', 'precio', 'fecha_vencimiento']

class CaracteristicaForm(forms.Form):
    caracteristica = forms.CharField(max_length=100, label="Característica")
