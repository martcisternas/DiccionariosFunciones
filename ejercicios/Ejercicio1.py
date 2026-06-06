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

            if nombre == "" in nombre:
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

    def mostrar_productos(productos):
        if productos == {}:
            print("No existen productos registrados.")
            return
        else:
            print(productos)

    def buscar_producto(productos):
        if productos == {}:
            print("No existen productos registrados.")
            return
        producto = input("Ingrese el producto a buscar: ")
        if producto in productos:
            print("El producto que busca si existe.")
        else:
            print("No se encotro el producto que buscado.")
            return
        
    def producto_mas_caro(productos):
        if len(productos) == 0:
            print("No existen productos")
            return
        mayor = 0
        nombreMayor = ""

        for nombre in productos:
            precio = productos[nombre][1]

            if precio > mayor:
                mayor = precio
                nombreMayor = nombre
        print(f"El producto más caro es {nombreMayor}")
        print(f"Su valor es {mayor}")
    
    if op == 1:
        print("Agregando productos...")
        agregar_producto(productos)
        print("Producto Agregado con exito!")

    if op == 2:
        print("Mostrando Productos...")
        print()
        mostrar_productos(productos)
    
    if op == 3:
        print("Buscando Producto...")
        buscar_producto(productos)

    if op == 4:
        print("El producto más caro es: ")
        producto_mas_caro(productos)

    if op == 5:
        print("Gracias por usar el programa, ¡Vuelva pronto!")





    