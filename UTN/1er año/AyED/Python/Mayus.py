def mayus(cadena):
    cadena_mayus = ""
    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
            cadena_mayus += cadena[i].upper()
        else:
            cadena_mayus += cadena[i] 

    return cadena_mayus

cadena = str(input("Ingrese una cadena: ").lower())
print(mayus(cadena))