# Gestión de Productos

Este proyecto es una aplicación web desarrollada con Django para gestionar productos, permitiendo registrar, consultar y almacenar información sobre cada producto.

## Tabla de Contenidos
1. [Características](#características)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Configuración del Entorno](#configuración-del-entorno)
4. [Uso](#uso)

## Características

- Registro de productos con los siguientes campos:
  - Nombre
  - Marca
  - Código
  - Fecha de Vencimiento (formato DD-MM-YYYY)
  - Precio
- Consulta de todos los productos registrados.
- Interfaz amigable para el usuario.

## Tecnologías Utilizadas

- [Python](https://www.python.org/) - Lenguaje de programación.
- [Django](https://www.djangoproject.com/) - Framework web.
- [SQLite](https://www.sqlite.org/) - Base de datos por defecto.

## Configuración del Entorno

1. **Clona el repositorio:**
   ```bash
   git clone <(https://github.com/Menkion/TI2041-2024.git)>

## Uso

### Registro de Productos

1. **Acceder al formulario de registro:**
   - Navega a la página de registro (`http://127.0.0.1:8000/productos/`).
  
2. **Completar el formulario:**
   - **Nombre:** Introduce el nombre del producto (ejemplo: "Galletas").
   - **Marca:** Especifica la marca del producto (ejemplo: "Brand A").
   - **Código:** Ingresa un código único para el producto (ejemplo: "GAL123").
   - **Fecha de Vencimiento:** Introduce la fecha de vencimiento en el formato `DD-MM-YYYY` (ejemplo: "01-01-2025").
   - **Precio:** Especifica el precio del producto (ejemplo: "2.50").

3. **Guardar el producto:**
   - Haz clic en el botón "Guardar Producto" para registrar el producto.

### Consulta de Productos

- Para ver todos los productos registrados, dirígete a la página de consulta. Allí se mostrará una lista con todos los productos ingresados, incluyendo todos los detalles (nombre, marca, código, fecha de vencimiento y precio).

