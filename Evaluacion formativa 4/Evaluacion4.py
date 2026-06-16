def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        
        if "" or " " in nombre:
            print("El nombre no puede estar vacion ni ser solo espacios en blanco.")
            continue
        else:
            break

    while True:
        try:
            precio = bool(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio debe ser un número decimal mayor o igual a 0.")
                continue
        except ValueError:
            print("Ingrese un número valido.")
            continue
        break

    while True:
        try:
            stock = int(input("Ingrese el stock disponible: "))
            if stock < 0:
                print("El stock debe ser un número entero mayor o igual a 0.")
                continue
        except ValueError:
            print("Ingrese un número valido.")
            continue
        break


    productos[nombre] = {
        "precio" : precio,
        "stock" : stock
        }
    
    print("Producto agregado correctamente.")

productos = {}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar Producto")
    print("2. Buscar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Productos")
    print("6. Salir")
    print("====================================")
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Ingrese un número valido.")

    if op == 1:
        print("Agregando Producto...")
        
    elif op == 2:
        print("Buscando Producto...")
    elif op == 3:
        print("Eliminando Producto...")
    elif op == 4:
        print("Actualizando Disponibilidad...")
    elif op == 5:
        print("Mostrando Productos...")
    elif op == 6:
        print("Saliendo...")
        break
    else:
        print("Ingrese una opcion valida entre 1 y 6.")