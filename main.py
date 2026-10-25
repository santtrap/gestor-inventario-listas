productos = []
cantidades = []

def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if nombre in productos:
        print("El producto ya existe.")
    else:
        cantidad = int(input("Cantidad disponible: "))
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado correctamente.")

def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO ---")
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]} - {cantidades[i]}")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in productos:
        i = productos.index(nombre)
        print(f"Encontrado: {productos[i]} con {cantidades[i]} unidades.")
    else:
        print("El producto no se encuentra.")

def modificar_cantidad():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        mostrar_inventario()
        pos = int(input(f"Número del producto a modificar (1-{len(productos)}): "))
        if pos >= 1 and pos <= len(productos):
            nueva = int(input("Ingrese la nueva cantidad: "))
            cantidades[pos - 1] = nueva
            print("Cantidad modificada con éxito.")
        else:
            print("Posición no válida.")

def eliminar_producto():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        mostrar_inventario()
        pos = int(input(f"Número del producto a eliminar (1-{len(productos)}): "))
        if pos >= 1 and pos <= len(productos):
            p = productos.pop(pos - 1)
            cantidades.pop(pos - 1)
            print(f"Producto '{p}' eliminado correctamente.")
        else:
            print("Posición no válida.")

def mostrar_total_productos():
    print(f"Cantidad de productos diferentes: {len(productos)}")

def mostrar_mayor_cantidad():
    if len(cantidades) == 0:
        print("El inventario está vacío.")
    else:
        max_c = max(cantidades)
        i = cantidades.index(max_c)
        print(f"Mayor cantidad: {productos[i]} ({max_c} unidades).")

def menu():
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar cantidad")
        print("5. Eliminar producto")
        print("6. Mostrar total de productos")
        print("7. Mostrar producto con mayor cantidad")
        print("8. Salir")
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_total_productos()
        elif opcion == "7":
            mostrar_mayor_cantidad()
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
