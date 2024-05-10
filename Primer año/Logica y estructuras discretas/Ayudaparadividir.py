def decodificar(p1):
    if p1=="0":
        p1=int(0)

    if p1=="1":
        p1=int(1)
        
    if p1=="2":
        p1=int(2)

    if p1=="3":
        p1=int(3)

    if p1=="4":
        p1=int(4)

    if p1=="5":
        p1=int(5)

    if p1=="6":
        p1=int(6)

    if p1=="7":
        p1=int(7)

    if p1=="8":
        p1=int(8)

    if p1=="9":
        p1=int(9)

    if p1=="A":
        p1=int(10)

    if p1=="B":
        p1=int(11)

    if p1=="C":
        p1=int(12)

    if p1=="D":
        p1=int(13)

    if p1=="E":
        p1=int(14)

    if p1=="F":
        p1=int(15)

    return p1
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
def polinomio_de_transformacion(valor_posicion, posicion, base):
    n=valor_posicion*base**posicion

    return n
#numero_pasado es requerido para que la funcion pasar_decimal corrá por la sumatoria de el numero al final
numero_pasado=""
numero_octal=str()
numero_binario=str()
numero_binario2=str()
caracter=str()
resultado=int()
valor=int()
numero_alrevez=str()
contador_de_0=int()
numero=str(input("Ingrese su dividendo (HEXADECIMAL): ")).upper()
numero2=str(input("Ingrese su divisor(OCTAL): ")).upper()

for caracter in numero:
    numero_alrevez=caracter+numero_alrevez
for i in range(len(numero_alrevez)):
        caracter=numero[i:i+1]
        numero_decimal=decodificar(caracter)
        valor=polinomio_de_transformacion(numero_decimal, i, 16)
        resultado=resultado+valor
numero_binario=pasar_decimal(resultado, 2, numero_pasado)
resultado=0
numero_alrevez=""
for caracter in numero2:
    numero_alrevez=caracter+numero_alrevez
    for i in range(len(numero_alrevez)):
        caracter=int(numero_alrevez[i:i+1])
        numero_decimal=polinomio_de_transformacion(caracter,i,8)
        resultado=resultado+numero_decimal
numero_binario2=pasar_decimal(resultado, 2, numero_pasado)

while len(numero_binario)>len(numero_binario2):
        numero_binario2+="0"
        contador_de_0+=1

print("La cantidad de digitos que tiene el cociente es: ",contador_de_0+1)
print("La resta que hay que realizar es: ",numero_binario,"-",numero_binario2)
