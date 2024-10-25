# Proyecto de Gestión de Productos

Este es un proyecto de Django para la gestión de productos, incluyendo características, marcas y categorías.

## Requisitos

- Python 3.8 o superior
- Django 4.0 o superior
- SQLite (incluido con Django)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
Crear un entorno virtual: python -m venv venv

Activar el entorno virtual:

En Windows: venv\Scripts\activate
En macOS/Linux: source venv/bin/activate

Instalar las dependencias: pip install -r requirements.txt
Aplicar migraciones: python manage.py migrate
Crear un superusuario (opcional, pero recomendado): python manage.py createsuperuser
Ejecutar el servidor: python manage.py runserver

Acceder a la aplicación:

Abre tu navegador y ve a http://127.0.0.1:8000/productos/.

Instrucciones de Uso
Para agregar productos, utiliza el formulario disponible en la página principal.
Puedes listar y filtrar productos, así como ver sus características.
Accede al panel de administración de Django en http://127.0.0.1:8000/admin/ utilizando las credenciales del superusuario que creaste.
