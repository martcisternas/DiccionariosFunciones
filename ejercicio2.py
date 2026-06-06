def agregar_alumno(alumnos):
    '''En esta funcion ingresaremos un nombre alumno con sus notas.'''
    nombre = input("Ingrese nombre del alumno: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return
    
    if nombre in alumnos:
        print("El alumno ya existe.")
        return
    
    if nombre.isdigit():
        print("El nombre debe ser con letras!")
        return
    
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de notas: "))
            break
        except ValueError:
            print("Ingrese un numero valido y entero.")

    notas = []

    for i in range(cantidad):
        print(f"Ingresando nota {i+1}/{cantidad}")
        notaParcial= validarNota()
        notas.append(notaParcial)

    alumnos[nombre] = notas
    print("Alumno agregado correctamente!.")

def validarNota():
    while True:
        try:
            nota = float(input("Ingrese nota: "))
            if nota >= 1.0 and nota <= 7.0:
                return nota
            print("La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Debe ingresar un valor valido!.")

def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return

    for nombre in alumnos:
        print(nombre,":", alumnos[nombre])

def ver_promedios(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        print(f"{nombre}, tiene un promedio de: {round(promedio,2)}")

def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return
    
    mayor = 0
    mejorAlumno = ""
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        
        if promedio > mayor:
            mayor = promedio
            mejorAlumno = nombre

    print(f"Mejor alumno es: {mejorAlumno}, con promedio {round(mayor,2)}") 

def cantidad_aprobados(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!")
        return
    
    aprobados = 0
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])

        if promedio >= 4.0:
            aprobados = aprobados + 1

    
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
        agregar_alumno(alumnos)
    elif op == 2:
        mostrar_alumnos(alumnos)
    elif op == 3:
        ver_promedios(alumnos)
    elif op == 4:
        mejor_alumno(alumnos)
    elif op == 5:
        cantidad_aprobados(alumnos)
    elif op == 6:
        print("Saliendo...")
    else:
        print("Opcion no valida.")
        break
