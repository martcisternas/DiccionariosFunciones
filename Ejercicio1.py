productos = {}

while True:
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Buscar Producto")
    print("4. Producto más caro")
    print("5. Salir")

    try:
        op = int(input("Ingrese una opcion: "))
        if op <= 0:
            print("Ingrese una opcion valida entre 1 y 5.")
            continue

        if op > 5:
            print("Ingrese una opcion valida entre 1 y 5.")
            continue
    except ValueError:
        print("Ingrese un número valido.")
        continue

    def agregar_producto(productos):
        '''Una funcion que permite agregar productos al diccionario "Productos"'''
        while True:
            nombre = input("Ingrese el nombre del producto: ")

            if " " in nombre:
                print("El nombre del producto no puede estar vacio.")
                continue

            if nombre in productos:
                print("No puede agregar un producto repetido.")
                continue

            try:
                stock = int(input("Ingrese la cantidad de stock a agregar: "))
                if stock < 0:
                    print("El stock debe ser mayor o igual a 0.")
                    continue
            except ValueError:
                print("Ingrese un número valido.")
                continue    
            
            try:
                precio = int(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("El precio debe ser un número mayor a 0.")
                    continue
            except ValueError:
                print("Ingrese un número valido.")
                continue
            break

        productos[nombre] = [stock, precio]

    if op == 1:
        print("Agregando productos...")
        agregar_producto(productos)
        print("Producto Agregado con exito!")



    