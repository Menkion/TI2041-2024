from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)  # Asegúrate de que este campo esté aquí
    codigo = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    caracteristica = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=100)  # Asegúrate de que este campo esté definido correctamente
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='caracteristicas')

    def __str__(self):
        return self.caracteristica

class TipoCaracteristica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre