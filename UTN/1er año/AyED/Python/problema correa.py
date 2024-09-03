def letras_a(cadena):
    cad1 = ""
    for i in range(len(cadena)):
        if cadena[i] in {"a", "A"} and (cadena[i-1] == " " or i == 0):
            while i < len(cadena) and cadena[i] != " ":
                cad1 += cadena[i]
                i += 1
            if i < len(cadena) and cadena[i] == " ":
                cad1 += " "
           
    return cad1

print(letras_a(input("Ingrese una cadena: ")))
