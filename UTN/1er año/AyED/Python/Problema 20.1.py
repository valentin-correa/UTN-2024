def telefono(cadena):
    cad_frmt = ""
    for i in range(4, 13):
        cad_frmt += cadena[i]

    return cad_frmt

cadena = str(input("Ingrese un número con formato: "))
print(telefono(cadena))