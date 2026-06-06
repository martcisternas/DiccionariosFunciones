import funciones as fn
#------ sistem ppal------
alumnos = {}

while True:
    print("-----MENU-----")
    print("1- Agregar alumno.")
    print("2- Mostrar alumno.")
    print("3- Ver promedio.")
    print("4- Mejor alumno.")
    print("5- Cantidad de aprobados.")
    print("6- Salir.")

    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Porfavor ingrese un numero valido.")

    if op == 1:
        fn.agregar_alumno(alumnos)
    elif op == 2:
        fn.mostrar_alumnos(alumnos)
    elif op == 3:
        fn.ver_promedios(alumnos)
    elif op == 4:
        fn.mejor_alumno(alumnos)
    elif op == 5:
        fn.cantidad_aprobados(alumnos)
    elif op == 6:
        print("Saliendo...")
    else:
        print("Opcion no valida.")
        break
