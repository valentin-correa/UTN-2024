cadena = str(input("Ingrese una cadena: "))
def Rev(cadena):
    cadenaRev = ""
    for i in range(len(cadena) - 1, -1, -1):
        cadenaRev += cadena[i]

    return cadenaRev

print(Rev(cadena))