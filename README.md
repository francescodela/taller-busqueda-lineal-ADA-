# Sistema de Tienda de Electrónica 

##  Descripción
Este proyecto lleva a cabo un sistema de administración para una tienda de dispositivos electrónicos empleando el algoritmo de **búsqueda lineal**. Posibilita la búsqueda de artículos y trabajadores mediante varios parámetros, administrar el inventario básico y verificar la disponibilidad de productos.

El sistema fue creado en **Python**, empleando listas de diccionarios para guardar la información de productos y trabajadores

---

##  Estructura del proyecto

- `datos_ejemplo.py` : Contiene los datos de prueba (productos y empleados).
- `funciones_busqueda.py` : Contiene todas las funciones de búsqueda lineal implementadas.
- `sistema_tienda.py` : Menú  que integra todas las funciones.
- `README.md` : Documentación del proyecto.
- `informe_taller.pdf` : Informe con análisis y conclusiones sobre la búsqueda lineal.

---

##  Funcionalidades

### Productos
- Buscar producto por **nombre** o **ID**.
- Buscar productos por **categoría** o **marca**.
- Buscar productos disponibles (**stock > 0**).
- Buscar productos dentro de un **rango de precios**.

### Empleados
- Buscar empleado por **nombre completo**.
- Buscar empleados por **departamento**.
- Listar empleados **activos**.

### Sistema
- Menú interactivo con submenús.
- Validación básica de entradas.
- Manejo de errores sencillo.

---

##  Cómo usar

1. Asegúrate de tener **Python 3** instalado.
2. Clona o descarga el repositorio.
3. Ejecuta el archivo principal:
```bash
python sistema_tienda.py
