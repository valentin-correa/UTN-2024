def comas(cadena):
    cadena_comas=""
    for i in range(len(cadena)):
       if i+1 != len(cadena):
            cadena_comas += cadena[i] + ","
       else:
            cadena_comas += cadena[i]

    return cadena_comas

def formato(cadena):
    cadena_formato = ""
    for i in range(len(cadena)):
        if cadena[i] == " ":
            cadena_formato += "_"
        else:
            cadena_formato += cadena[i]

    return cadena_formato

def password(cadena):
    cadena_x = ""
    i = 0
    while i < (len(cadena)):
        cadena_x += "X"
        i += 1

    return print("Su clave es: " + cadena_x)

def puntos(cadena):
    cadena_puntos = ""
    for i in range(len(cadena)):
        if i % 3 == 0 and i != 0:
            cadena_puntos += "."
        else:
            cadena_puntos += cadena[i]

    return cadena_puntos

cadena = str(input("Ingrese una cadena: "))
caract = str(input("Ingrese una función (| , | _ | X | . |: "))
if caract == ",":
    print(comas(cadena))
if caract == "_":
    print(formato(cadena))
if caract == "X":
    print(password(cadena))
if caract == ".":
    print(puntos(cadena))    