# sistemaTienda.py
# Sistema interactivo de la tienda 
# Permite búsquedas de productos y empleados con menús

from datos_ejemplo import productos, empleados
from funciones_busqueda import *

# ------------------------------
# Menú principal
# ------------------------------
def menuPrincipal():
    while True:
        print("\n--- tienda de tecnologia ---\n"
            "1. Buscar producto\n"
            "2. Buscar empleado\n"
            "3. Buscar productos por disponibilidad y filtros\n"
            "4. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenuBusquedaProducto()
        elif opcion == "2":
            submenuBusquedaEmpleado()
        elif opcion == "3":
            submenuBusquedaFiltros()
        elif opcion == "4":
            print("¡Gracias por usar esta aplicacion !")
            break
        else:
            print("Opción inválida, intente de nuevo.")


# Submenú de búsqueda de productos

def submenuBusquedaProducto():
    print("\n--- BÚSQUEDA DE PRODUCTO ---\n"
      "1. Por nombre\n"
      "2. Por ID\n"
      "3. Por categoría\n")
      
    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        resultado = buscarProductoPorNombre(productos, nombre)
        print(resultado if resultado else "Producto no encontrado")
    elif opcion == "2":


        try:
            idProducto = int(input("Ingrese el ID del producto: "))
            resultado = buscarProductoPorId(productos, idProducto)
            print(resultado if resultado else "Producto no encontrado")
        except ValueError:


            print("ID inválido")
    elif opcion == "3":
        categoria = input("Ingrese la categoría: ")
        resultados = buscarProductosPorCategoria(productos, categoria)
        print(resultados if resultados else "No se encontraron productos")
    else:
        print("Opción inválida")

# ------------------------------
# Submenú de búsqueda de empleados
# ------------------------------
def submenuBusquedaEmpleado():
    print("\n--- BÚSQUEDA DE EMPLEADO ---")
    print("1. Por nombre completo")
    print("2. Por departamento")
    print("3. Empleados activos")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        resultado = buscarEmpleadoPorNombre(empleados, nombre, apellido)
        print(resultado if resultado else "Empleado no encontrado")
    elif opcion == "2":
        departamento = input("Departamento: ")
        resultados = buscarEmpleadosPorDepartamento(empleados, departamento)
        print(resultados if resultados else "No se encontraron empleados")
    elif opcion == "3":
        resultados = buscarEmpleadosActivos(empleados)
        print(resultados if resultados else "No hay empleados activos")
    else:
        print("Opción inválida")

# ------------------------------
# Submenú de filtros y disponibilidad
# ------------------------------
def submenuBusquedaFiltros():
    print("\n--- BÚSQUEDA POR DISPONIBILIDAD Y FILTROS ---\n"
      "1. Productos disponibles\n"
      "2. Productos por rango de precio\n"
      "3. Productos por marca\n"
      "4. Contar productos por categoría\n")
    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        resultados = productosDisponibles(productos)
        print(resultados)
    elif opcion == "2":
        try:
            minimo = float(input("Precio mínimo: "))
            maximo = float(input("Precio máximo: "))
            resultados = buscarProductosPorRangoPrecio(productos, minimo, maximo)
            print(resultados)
        except ValueError:
            print("Precio inválido")
    elif opcion == "3":
        marca = input("Ingrese la marca: ")
        resultados = buscarProductosPorMarca(productos, marca)
        print(resultados)
    elif opcion == "4":
        categoria = input("Ingrese la categoría: ")
        cantidad = contarProductosPorCategoria(productos, categoria)
        print(f"Cantidad de productos en {categoria}: {cantidad}")
    else:
        print("Opción inválida")

# ------------------------------
# Inicio del programa
# ------------------------------
if __name__ == "__main__":
    menuPrincipal()
