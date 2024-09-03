def consotantes(cadena):
    cadena_cons = ""
    for i in range(len(cadena)):
        if cadena[i] != "a" and cadena[i] != "e" and cadena[i] != "i" and cadena[i] != "o" and cadena[i] != "u": 
            cadena_cons += cadena[i]
       
    return cadena_cons

def vocales(cadena):
    cadena_voc = ""
    for i in range(len(cadena)):
        if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u": 
            cadena_voc += cadena[i]
       
    return cadena_voc

def vocvoc(cadena):
    cadena_vocvoc = ""
    for i in range(len(cadena)):
        if cadena[i] == "a":
            cadena_vocvoc += "e"
        if cadena[i] == "e":
            cadena_vocvoc += "i"
        if cadena[i] == "i":
            cadena_vocvoc += "o"
        if cadena[i] == "o":
            cadena_vocvoc += "u"
        if cadena[i] == "u":
            cadena_vocvoc += "a"
        if cadena[i] != "a" and cadena[i] != "e" and cadena[i] != "i" and cadena[i] != "o" and cadena[i] != "u": 
            cadena_vocvoc += cadena[i]

    return cadena_vocvoc

def palid(cadena):
    cadena_palid = ""
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_palid += cadena[i]
    if cadena_palid == cadena_palid[::-1]:
        print('"' + cadena_palid + '"' + " es un palídromo")
    else:
        print('"' + cadena + '"' + " NO es un palídromo")
    
cadena = str(input("Ingrese una cadena: "))
print(consotantes(cadena))
print(vocales(cadena))
print(vocvoc(cadena))
(palid(cadena))