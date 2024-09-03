def may_men(cadena1, cadena2):
    if len(cadena1) > len(cadena2):
        return "La cadena 1 es mayor a la 2"
    else:
        return "La cadena 2 es mayor a la 1"

def mayus1(cadena1):
    cadena_mayus=""
    for i in range(len(cadena1)):
        if cadena1[i] == "a" or cadena1[i] == "e" or cadena1[i] == "i" or cadena1[i] == "o" or cadena1[i] == "u":
            cadena_mayus += cadena1[i].upper()
        else:
            cadena_mayus += cadena1[i]
        
    return cadena_mayus
        
def mayus2(cadena2):
    cadena_mayus2=""
    for i in range(len(cadena2)):
        if cadena2[i] != "a" and cadena2[i] != "e" and cadena2[i] != "i" and cadena2[i] != "o" and cadena2[i] != "u":
            cadena_mayus2 += cadena2[i].upper()
        else:
            cadena_mayus2 += cadena2[i]
    
    return cadena_mayus2

def concat(cadena1, cadena2):
    cadena3 = (mayus1(cadena1)) + (mayus2(cadena2))
    return cadena3

def concatRev(cadena1, cadena2):
    cadena3 = (mayus1(cadena1)) + (mayus2(cadena2))
    for i in range(len(cadena3)):
        cadena3_rev = cadena3[::-1]
    
    return cadena3_rev

cadena1=str(input("Ingrese un texto: "))
cadena2=str(input("Ingrese otro texto: "))

print(cadena1, cadena2)
print(mayus1(cadena1), mayus2(cadena2))
print(concat(cadena1, cadena2))
print(concatRev(cadena1, cadena2))