'''usuarios = {
    "juan" : ["M","qwertyuiop"],
    "maria" : ["F", "fasdasdf2"]
}
#Usaremos este para el ejercicio
usuario2 = {
    "daniel":{
        "sexo":"M",
        "pass":"1234asdf"
    },
    "jorge:{"
    "sexo":"M",
    "pass":"4567asdf"
    }

'''
#funciones

def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ")

        if nombre in usuarios:
            print("Usuario ya existe, intente con otro nombre.")
        else:
            break

    while True:
        sexo = input("Ingrese sexo(M,F): ").upper()

        if sexo == "M" or sexo == "F":
            break
        else:
            print("El sexo debe ser M o F, Ingrese nuevamente!")

    while True:
        contraseña = input("Ingrese contraseña: ")
        
        if validar_contraseña(contraseña):
            #print("Contraseña Válida")
            break
        else:
            print("Contraseña inválida, debe tener 8 caracteres entre letras y números")

    #Agregue el usuario con diccionarios.
    usuarios[nombre] = {
        "sexo" : sexo,
        "contraseña" : contraseña
    }
    print("Usuario ingresado correctamente!")

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    
    if " " in contraseña:
        return False
    
    num = False
    letra = False

    for caracter in contraseña:
        if caracter.isdigit():
            num = True
        if caracter.isalpha():
            letra = True

    return num and letra

def buscar_usuario():
    nombre = input("Ingrese nombre a buscar: ")

    if nombre in usuarios:
        print("Sexo: ",usuarios[nombre]["sexo"])
        print(f"Contraseña: {usuarios[nombre]["contraseña"]}")
    else:
        print("Nombre no encontrado!")

def eliminar_usuario():
    nombre = input("Ingrese nombre a buscar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado!")
    else:
        print("Nombre no encontrado!")

#parte ppal
usuarios ={}

while True:
    print("--- Menu Principal ---")
    print("1. Ingresar Usuario.")
    print("2. Buscar Usuario.")
    print("3. Eliminar Usuario.")
    print("4. Salir")

    while True:
        try:
            op = int(input("Ingrese una opción"))
            break
        except ValueError:
            print("Por favor ingrese una opción válida!")

    if op == 1:
        ingresar_usuario()
    elif op == 2:
        buscar_usuario()
    elif op == 3:
        eliminar_usuario()
    elif op == 4:
        print("Saliendo...")
        break
    else:
        print("Ingrese una opcion valida entre 1 y 4.")

                 
    
