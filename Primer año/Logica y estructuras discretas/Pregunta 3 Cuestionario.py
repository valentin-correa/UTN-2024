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
def codificador(num):
    if num==0:
        num="0"
    if num==1:
        num="1"
    if num==2:
        num="2"
    if num==3:
        num="3"
    if num==4:
        num="4"
    if num==5:
        num="5"
    if num==6:
        num="6"
    if num==7:
        num="7"
    if num==8:
        num="8"
    if num==9:
        num="9"
    if num==10:
        num="A"
    if num==11:
        num="B"
    if num==12:
        num="C"
    if num==13:
        num="D"
    if num==14:
        num="E"
    if num==15:
        num="F"
    return num
def polinomio_de_transformacion(valor_posicion, posicion, base):
    n=valor_posicion*base**posicion

    return n
#numero_pasado es requerido para que la funcion pasar_decimal corrá por la sumatoria de el numero al final
numero_pasado=""

numero_octal=str()
numero_binario=str()
numero_decimal=int()
caracter=str()
resultado=int()
numero_hexadecimal=""
contador_de_4=int(4)
contador_de_3=int(3)
relleno=int()
contador=int()
numero_alrevez=str()
sistema_entrada=str(input("¿Que sistema va a ingresar?\n")).lower()
sistema_salida=str(input("¿A que sistema lo va a pasar?\n")).lower()
numero=str(input("Ingrese su numero: ")).upper()

if sistema_entrada=="binario":

    if sistema_salida=="decimal":
        for i in range(len(numero)):
            caracter=int(numero[i:i+1])
            numero_decimal=polinomio_de_transformacion(caracter,i,2)
            resultado=resultado+numero_decimal
        if i==len(numero)-1:
            print(resultado)

    if sistema_salida=="hexadecimal":
        resultado=0
        for i in range(len(numero)):
            relleno=len(numero)%4
            if relleno!=0:
                numero="0"+numero
        for i in range(len(numero)):
            contador_de_4-=1
            if contador_de_4!=4:
                contador+=1
                caracter=int(numero[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,contador_de_4,2)
                resultado=resultado+numero_decimal

                if contador==4:
                    numero_hexadecimal=numero_hexadecimal+codificador(resultado)
                    resultado=0
                    contador=0
                    contador_de_4=4

        if i==len(numero)-1:
            print(numero_hexadecimal)
        
    if sistema_salida=="octal":
        resultado=0
        for i in range(len(numero)):
            relleno=len(numero)%3
            if relleno!=0:
                numero="0"+numero
        for i in range(len(numero)):
            contador_de_3-=1
            if contador_de_3!=3:
                contador+=1
                caracter=int(numero[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,contador_de_3,2)
                resultado=resultado+numero_decimal

                if contador==3:
                    numero_octal=numero_octal+str(resultado)
                    resultado=0
                    contador=0
                    contador_de_3=3
        if i==len(numero)-1:
            print(numero_octal)
if sistema_entrada=="octal":
        if sistema_salida=="decimal":
            for i in range(len(numero)):
                caracter=int(numero[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,i,8)
                resultado=resultado+numero_decimal
            if i==len(numero)-1:
                print(resultado)

        if sistema_salida=="binario":
            for caracter in numero:
                numero_alrevez=caracter+numero_alrevez
            for i in range(len(numero_alrevez)):
                caracter=int(numero_alrevez[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,i,8)
                resultado=resultado+numero_decimal
                numero_binario=pasar_decimal(resultado, 2, numero_pasado)
            print(numero_binario)
        
        if sistema_salida=="hexadecimal":
            for i in range(len(numero)):
                caracter=int(numero[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,i,8)
                resultado=resultado+numero_decimal
            
            numero_binario=numero_binario+pasar_decimal(resultado, 2, numero_pasado)
            resultado=0
            for i in range(len(numero_binario)):
                relleno=len(numero_binario)%4
                if relleno!=0:
                    numero_binario="0"+numero_binario
            for i in range(len(numero_binario)):
                contador_de_4-=1
                if contador_de_4!=4:
                    contador+=1
                    caracter=int(numero_binario[i:i+1])
                    numero_decimal=polinomio_de_transformacion(caracter,contador_de_4,2)
                    resultado=resultado+numero_decimal

                    if contador==4:
                        numero_hexadecimal=numero_hexadecimal+codificador(resultado)
                        resultado=0
                        contador=0
                        contador_de_4=4
            if i==len(numero_binario)-1:
                print(numero_hexadecimal)
if sistema_entrada=="decimal":
    numero_decimal=int(numero)

    if sistema_salida=="binario":
        numero_binario=numero_binario+pasar_decimal(numero_decimal, 2, numero_pasado)
        print(numero_binario)
    if sistema_salida=="hexadecimal":
        numero_binario=numero_binario+pasar_decimal(numero_decimal, 2, numero_pasado)
        resultado=0
        for i in range(len(numero_binario)):
            relleno=len(numero_binario)%4
            if relleno!=0:
                numero_binario="0"+numero_binario
        for i in range(len(numero_binario)):
            contador_de_4-=1
            if contador_de_4!=4:
                contador+=1
                caracter=int(numero_binario[i:i+1])
                numero_decimal=polinomio_de_transformacion(caracter,contador_de_4,2)
                resultado=resultado+numero_decimal

                if contador==4:
                    numero_hexadecimal=numero_hexadecimal+codificador(resultado)
                    resultado=0
                    contador=0
                    contador_de_4=4
        if i==len(numero_binario)-1:
            print(numero_hexadecimal)
    if sistema_salida=="octal":
        numero_octal=numero_octal+pasar_decimal(numero_decimal, 8, numero_pasado)
        print(numero_octal)
if sistema_entrada=="hexadecimal":
    for caracter in numero:
        numero_alrevez=caracter+numero_alrevez
    for i in range(len(numero_alrevez)):
        caracter=numero_alrevez[i:i+1]
        numero_decimal=decodificar(caracter)
        valor=polinomio_de_transformacion(numero_decimal, i, 16)
        resultado=resultado+valor
        
        if sistema_salida=="binario":

            numero_binario=pasar_decimal(resultado, 2, numero_pasado)
            if i==len(numero)-1:
                print(numero_binario)

        if sistema_salida=="decimal":
            if i==len(numero)-1:
                print(resultado)

        if sistema_salida=="octal":
            numero_octal=pasar_decimal(resultado, 8, numero_pasado)
            if i==len(numero)-1:
                print(numero_octal)