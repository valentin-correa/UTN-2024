def leftTrim(cadena):
    cad_clean = ""
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cad_clean += cadena[i]

    return cad_clean

cadena = str(input("Ingrese una cadena: "))
print(leftTrim(cadena))