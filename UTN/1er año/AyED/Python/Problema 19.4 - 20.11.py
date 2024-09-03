def separador(num):
    cadena_num = ""
    num = num[::-1]
    for i in range(len(num)):
        if i % 3 == 0 and i != 0:
            cadena_num += "." + num[i]
        else:
            cadena_num += num[i]

    cadena_num = cadena_num[::-1]
    return cadena_num

num = str(input("Ingrese un número: "))
print(separador(num))