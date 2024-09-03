def siglas(cadena):
    siglas = ""
    for i in range(len(cadena)):
        cadena_mayus = ""
        if i == 0:
            siglas += cadena[i].upper()
        if cadena[i] == " ":
            siglas += cadena[i+1].upper()
            cadena_mayus += cadena[i+1].upper()

    return siglas

def mayus(cadena):
    x = False
    cadena_mayus = ""
    for i in range(len(cadena)):
        if cadena[i-1] == " " or i == 0:
            x = True
        if x == True and (cadena[i-1] == " " or i == 0):
            cadena_mayus += cadena[i].upper()
        else:
            cadena_mayus += cadena[i]
        if cadena[i] == " ":
            x = False

    return cadena_mayus

def palA(cadena):
    x = False
    cadena_a = ""
    for i in range(len(cadena)):
        if (cadena[i] == "a" or cadena[i] == "A") and (cadena[i-1] == " " or i == 0):
            x = True
        if x == True:
            cadena_a += cadena[i]
        if cadena[i] == " ":
            x = False
       

    return cadena_a          

cadena = str(input("Ingrese una cadena: "))
print(siglas(cadena))
print(mayus(cadena))
print(palA(cadena))