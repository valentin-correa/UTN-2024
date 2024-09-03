def vocmayus(cadena, vocal):
    cad_mayus = ""
    for i in range(len(cadena)):
        if cadena[i] == vocal:
            cad_mayus += cadena[i].upper()
        else:
            cad_mayus += cadena[i]

    return cad_mayus

cadena = str(input("Ingrese una cadena: "))
vocal = str(input("Ingrese una vocal: "))
print(vocmayus(cadena, vocal))