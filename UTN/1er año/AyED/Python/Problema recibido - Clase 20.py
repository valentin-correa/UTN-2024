ac = 0
cadena = str(input("Ingrese una cadena: "))
for i in range(len(cadena)):
    if cadena[i] in {"a", "e", "i", "o", "u"}  and (cadena[i-1] == " " or i == 0): 
        ac += 1

print("La cantidad de palabras que comienzan con una vocal es: ", ac)


