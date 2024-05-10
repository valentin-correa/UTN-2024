def espacios_acomodador(cadena):
    cadena_good = ""
    for i in range(len(cadena)):
        if cadena[i] != " " or (cadena[i] == " " and cadena[i-1] != " "):
            cadena_good += cadena[i]
    return cadena_good

def dificultad():
    palabraCONTADOR=int()
    espacios=[0]
    statement=str(input())
    CantidadPalabras=0
    TotalLetras=0
    Promedio=0
    puntaje=0
    statement=espacios_acomodador(statement)
    for i in range(len(statement)):
        if statement[i]==" " and statement[i+1]!=" ":
            espacios.append(str(i))
            palabraCONTADOR+=1
    letras=cantidadLetras(espacios)
    for i in range(len(letras)):
        TotalLetras+=letras[i]
    CantidadPalabras=len(espacios)//2
    Promedio=TotalLetras//CantidadPalabras

    if Promedio<=3:
        puntaje=250
    if Promedio==4 or Promedio==5:
        puntaje=500
    if Promedio>=6:
        puntaje=1000
    return puntaje



def cantidadLetras(posEspacios):
    letras=[]
    for i in range(len(posEspacios)):
        letras.append(abs(int(posEspacios[i])-int(posEspacios[i+1])))
    return letras




def validate(texto, espacios):
    for i in range(len(texto)):
        if texto[espacios[i]:espacios[i+1]] in {"0","1","2","3","4","5","6","7","8","9",",","."}:
            return False
    return True
print(dificultad())