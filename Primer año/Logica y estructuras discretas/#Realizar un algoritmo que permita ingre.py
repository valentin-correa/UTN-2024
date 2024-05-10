#Realizar un algoritmo que permita ingresar un numero en Hexadecimal y pasarlo al sistema Octal
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
def polinomio_de_transformacion(valor_posicion, posicion, base):
    n=valor_posicion*base**posicion

    return n
def pasar_decimal(numero_decimal, base):
    cociente=int
    resto=int
    numero_pasado=""
    cociente=numero_decimal//base
    resto=numero_decimal%base
    restostr=str(resto)
    numero_pasado=restostr + numero_pasado

    if cociente>=base:
        numero_pasado=pasar_decimal(cociente, base)
    return numero_pasado

sub1=str()
numero_decimal=int()
resultado=int()
cad1=str(input()).upper()

for i in range(len(cad1)):
    sub1=cad1[i:i+1]
    numero_decimal=decodificar(sub1)

    valor=polinomio_de_transformacion(numero_decimal, i, 16)

    resultado=resultado+valor

print(pasar_decimal(resultado, 8))






