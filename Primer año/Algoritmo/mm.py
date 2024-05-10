def dificultad(statement):
    palabras = dividir_en_palabras(statement)
    acB=0
    suma_longitudes = 0

    for palabra in palabras:
        longitud_palabra = obtener_longitud_palabra(palabra)
        if longitud_palabra==0:
            acB+=1
        suma_longitudes += longitud_palabra

    if len(palabras) == 0:
        promedio = 0
    else:
        if (len(palabras)-acB)<=0 or suma_longitudes == 0:
            promedio = 0
        else:
            promedio = int(suma_longitudes / (len(palabras)-acB))

    if promedio <= 3:
        return 250
    elif promedio <= 5:
        return 500
    else:
        return 1000

def dividir_en_palabras(statement):
    palabras = statement.split()
    return palabras

def obtener_longitud_palabra(palabra):
    longitud = contar_letras(palabra)
    return longitud

def contar_letras(palabra):
    ac= 0
    for i in range(len(palabra)):
        if palabra[i] in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","x","y","z","w","v"}:
            ac+= 1 #Si es una letra suma uno
        else:
            if i==(len(palabra)-1) and palabra[i]==".":
                return ac
            else:
                return 0 #Si no es una letra, cortá y devuelve 0 a no ser que sea la ultima posicion y justo la ultima sea un "."
    return ac


while True:
    try:        
        statement=str(input())
        print(dificultad(statement))
    except EOFError:
        break