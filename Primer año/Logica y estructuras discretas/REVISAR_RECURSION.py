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
    numero_pasado_end=str()
    numero_pasado=""
    while numero_decimal>0:
        resto=int()
        resto=numero_decimal%base
        numero_decimal=numero_decimal//base
        numero_pasado=numero_pasado + str(resto)

#Invierto la cadena para acomodarla
    for character in numero_pasado:
        numero_pasado_end=character+numero_pasado_end
    return numero_pasado_end

sub1=str()
numero_decimal=int()
resultado=int()
cad=str(input("Numero hexadecimal: ")).upper()
cad1=str()
#Invierto la cadena para acomodarla
for character in cad:
    cad1=character+cad1

for i in range(len(cad1)):
    sub1=cad1[i:i+1]
    numero_decimal=decodificar(sub1)

    valor=polinomio_de_transformacion(numero_decimal, i, 16)

    resultado=resultado+valor
    
print("Numero decimal: ", resultado)
print("Numero en octal: ", pasar_decimal(resultado, 8))