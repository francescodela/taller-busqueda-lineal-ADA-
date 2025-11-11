# Funciones de búsqueda lineal 

# Función de búsqueda lineal básica en una lista de elementos simples
def busquedaLinealElemento():
    """
    Busca un elemento en una lista usando búsqueda lineal
        lista: Lista de elementos (números, strings, etc.)
        elemento: Elemento que queremos buscar
    Returns:
        Índice del elemento si se encuentra, -1 si no
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1


# Funciones de búsqueda en productos

def buscarProductoPorNombre(productos, nombre):
    """
    Busca un producto por nombre
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None


def buscarProductoPorId(productos, idProducto):
    """
    Busca un producto por su ID
    """
    for producto in productos:
        if producto['id'] == idProducto:
            return producto
    return None


def buscarProductosPorCategoria(productos, categoria):
    """
    Devuelve una lista de productos en una categoría
    """
    resultados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            resultados.append(producto)
    return resultados


# Funciones de búsqueda en empleados

def buscarEmpleadoPorNombre(empleados, nombre, apellido):
    """
    Busca un empleado por nombre y apellido
    """
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre.lower() and empleado['apellido'].lower() == apellido.lower():
            return empleado
    return None


def buscarEmpleadosPorDepartamento(empleados, departamento):
    """
    Devuelve una lista de empleados de un departamento
    """
    resultados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower():
            resultados.append(empleado)
    return resultados


def buscarEmpleadosActivos(empleados):
    """
    Devuelve una lista de empleados activos
    """
    return [emp for emp in empleados if emp['activo']]


# Funciones de filtros en productos

def productosDisponibles(productos):
    """
    Devuelve productos que están disponibles (stock > 0)
    """
    return [prod for prod in productos if prod['stock'] > 0]


def buscarProductosPorRangoPrecio(productos, precioMin, precioMax):
    """
    Devuelve productos cuyo precio está entre precioMin y precioMax
    """
    return [prod for prod in productos if precioMin <= prod['precio'] <= precioMax]


def buscarProductosPorMarca(productos, marca):
    """
    Devuelve productos de una marca específica
    """
    return [prod for prod in productos if prod['marca'].lower() == marca.lower()]


def contarProductosPorCategoria(productos, categoria):
    """
    Retorna la cantidad de productos en una categoría
    """
    return len([prod for prod in productos if prod['categoria'].lower() == categoria.lower()])
