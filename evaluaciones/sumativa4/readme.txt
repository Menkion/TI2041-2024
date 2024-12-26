Descripción de la API
Esta API permite gestionar productos, incluyendo la creación, actualización, eliminación y consulta de productos.

Documentación de cada servicio y llamada
Crear Producto
Nombre del servicio: Crear Producto

Descripción: Este servicio permite crear un nuevo producto.

Método HTTP: POST

URL: /api/productos/create/

Entradas:

ProductoSerializer: Un objeto JSON que contiene los datos del producto a crear.

Salidas:

201 Created: Devuelve el objeto del producto creado.

400 Bad Request: Devuelve los errores de validación si los datos proporcionados no son válidos.
