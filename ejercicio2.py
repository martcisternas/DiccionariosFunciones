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
    
    cantidad = int(input("Ingrese cantidad de notas: "))

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
        print(alumnos)
