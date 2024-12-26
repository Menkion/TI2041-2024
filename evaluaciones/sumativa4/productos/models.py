from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuario Personalizado"
        verbose_name_plural = "Usuarios Personalizados"

    # Personalización de los campos de grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario'
    )

    # Método clean para normalizar el correo electrónico
    def clean(self):
        super().clean()
        if self.email:
            self.email = self.email.lower()  # Normaliza el correo
            email_validator = EmailValidator()
            try:
                email_validator(self.email)
            except ValidationError:
                raise ValidationError("El correo electrónico no es válido")
    

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
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    caracteristica = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='caracteristicas')

    def __str__(self):
        return self.nombre

class TipoCaracteristica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
