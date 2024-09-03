def espacios(cadena):
    cadena_good = ""
    for i in range(len(cadena)): 
        if cadena[i] != " " or (cadena[i] == " " and cadena[i + 1] != " "):
            cadena_good += cadena[i]
    return cadena_good

def nombres(cadena):
    cad_god = ""
    for i in range(len(cadena)):
        if cadena[i] not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            cad_god += cadena[i]
    return cad_god

cadena = "ame 50     union central 26"
print(nombres(espacios(cadena)))