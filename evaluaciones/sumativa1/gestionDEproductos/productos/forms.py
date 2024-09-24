from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'codigo', 'fecha_vencimiento', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Producto XYZ'}),
            'marca': forms.TextInput(attrs={'placeholder': 'Ej: Marca ABC'}),
            'codigo': forms.TextInput(attrs={'placeholder': 'Ej: 12345'}),
            'fecha_vencimiento': forms.TextInput(attrs={'placeholder': 'Ej: 2025-01-01'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ej: 999.999'}),
        }
