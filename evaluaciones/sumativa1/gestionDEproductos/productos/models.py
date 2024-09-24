from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=100, decimal_places=3)

    def __str__(self):
        return self.nombre