def pasar_decimal(numero_decimal, base, numero_pasado):
    cociente=int
    resto=int
    cociente=numero_decimal//base
    resto=numero_decimal%base
    restostr=str(resto)
    numero_pasado=restostr + numero_pasado

    if cociente>=base:
        numero_pasado=pasar_decimal(cociente, base, numero_pasado)

    if cociente<base:
        resto=cociente
        restostr=str(resto)
        numero_pasado=restostr + numero_pasado

    return numero_pasado
#numero_pasado es requerido para que pasar decimal corra por la sumatoria de el numero final
numero_pasado=""

#Declaracion de variables
num_bin=str()
sub1=str()
numero_decimal=int()

#ingreso de numero
cad1=str(input("Numero decimal:"))
numero_decimal=int(cad1)


num_bin=num_bin+pasar_decimal(numero_decimal, 2, numero_pasado)

print("Numero en binario:",num_bin)