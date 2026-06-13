def registrar_producto():
    while True:
        codigo = (input("Ingrese el codigo del producto: "))
        
        if codigo in productos:
            print("El codigo del producto no puede estar repetido.")
            continue
        else:
            break
    
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        
        if len(nombre) < 3:
            print("El nombre del producto debe contener al menos 3 caracteres.")
        else:
            break

    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Ingrese un número valido.")

    productos[codigo] = {
        "nombre" : nombre,
        "precio" : precio
        }
    
    print("Producto registrado correctamente.")

def buscar_producto():
    codigo = (input("Ingrese el codigo del producto a buscar: "))
    
    if codigo in productos:
        print(f"Código: {codigo}")
        print(f"Nombre: {productos[codigo]["nombre"]}")
        print(f"Precio: {productos[codigo]["precio"]}")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    codigo = (input("Ingrese el codigo del producto a elimnar: "))
    
    if codigo in productos:
        print(f"¿Estas seguro que quieres elimnar {productos[codigo]["nombre"]}?")
        verificar = input("Si / No: ").upper()
        if verificar == "SI":
            del productos[codigo]
            print("Producto elimnado exitosamente")
        elif verificar == "NO":
            print("Volviendo...")
            return
        else:
            print("Opcion no valida, volviendo...")
            return
    else:
        print("No fue posible eliminar el producto.")

productos = {}

while True:
    print("1.- Registrar producto.")
    print("2.- Buscar producto.")
    print("3.- Eliminar producto.")
    print("4.- Salir.")

    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Ingrese un número válido entre 1 y 4.")
            continue

    if op == 1:
        print("Registrando Producto...")
        registrar_producto()
    elif op == 2:
        print("Buscando Producto...")
        buscar_producto()
    elif op == 3:
        print("Eliminando Producto...")
        eliminar_producto()
    elif op == 4:
        print("Programa Finalizado...")
        break
