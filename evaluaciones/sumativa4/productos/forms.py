from django import forms
from .models import Producto, Caracteristica, CustomUser
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'categoria', 'codigo', 'precio', 'fecha_vencimiento']

class CaracteristicaForm(forms.Form):
    caracteristica = forms.CharField(max_length=100, label="Característica")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_staff', 'is_superuser')
