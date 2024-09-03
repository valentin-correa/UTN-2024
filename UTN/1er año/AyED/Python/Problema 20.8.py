cadena = str(input("Ingrese una cadena: "))
cadena_palid = ""
for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_palid += cadena[i]
if cadena_palid == cadena_palid[::-1]:
    print('"' + cadena_palid + '"' + " es un palídromo")
else:
    print('"' + cadena + '"' + " NO es un palídromo")