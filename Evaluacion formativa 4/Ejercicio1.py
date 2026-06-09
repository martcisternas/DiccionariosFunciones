def ingresar_usuario(usuarios):
    nombre = input("Ingrese nombre del usuario: ").strip()
    
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return
    
    if nombre in usuarios:
        print("El usuario ya existe.")
        return
    
    sexo = input("Ingrese el sexo del usuario (F / M): ").upper()

    if sexo == "F" or sexo == "M":
        print("Agregado correctamente...")
    else:
        print("Solo se permite (F o M).")
        return    
    
    contraseña = (input("Ingrese la contraseña del usuario: ")).strip()

    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 digitos.")
        return
    
    if contraseña == "":
        print("La constraseña no puede estar vacia.")
    
    for letra in contraseña:
        if letra.isdigit:
           return True
        else:
            print("La contraseña no tiene digitos.")
    
usuarios = {}




while True:
    print("-----MENU-----")
    print("1- Ingresar usuario.")
    print("2- Buscar usuario.")
    print("3- Eliminar usuario.")
    print("4- Salir.")

    try:
        op = int(input("Ingrese una opcion: "))

        if op > 4:
            print("Ingrese una opcion entre 1 y 4.")
            continue 
        if op < 1:
            print("Ingrese una opcion entre 1 y 4.")
            continue
    except ValueError:
        print("Ingrese un numero valido.")
        continue
    break
    

if op == 1:
    print("Ingresando Usuario...")
    ingresar_usuario(usuarios)

if op == 2:
    print("Buscando Usuario...")

if op == 3:
    print("Eliminando Usuario...")

if op == 4:
    print("Saliendo.")
