correo = str(input("Ingrese su correo electrónico: "))
cadena_form = ""
for i in range(len(correo)):
    if correo[i] != ".":
        cadena_form += correo[i]
    else:
        break

print(cadena_form +".ceu.es")