def separar(texto, separador):
    resultado = []
    inicio = 0
    i = 0
    for i in range(len(texto)):
        if texto[i] == separador:
            resultado.append(texto[inicio:i])
            inicio = i + 1
    i += 1
    resultado.append(texto[inicio:i])
    return resultado

def UnionConjuntos(A,B):

    #Eliminacion de la llave y colocacion de la coma para la union
    A = A[:-1] + ","
    B = B[1:]

    #Concatenacion de ambos conjuntos
    AuB = A + B
    
    #Elimino las llaves
    AuB = AuB[:-1]
    AuB = AuB[1:]
    
    #Ahora voy a transferir todos los caracteres entre "," a una lista

    conjunto = separar(AuB,",")

    #Saco los elementos repetidos
    conjuntoFinal = []

    for i in conjunto:
        if i not in conjuntoFinal:
            conjuntoFinal.append(i)

    #Lo formateo para imprimirlo en pantalla
    
    resultado = "{"
    VAR = len(conjuntoFinal)
    for i in range(VAR):    
        resultado += str(conjuntoFinal[i]) + ","
        if i == len(conjuntoFinal)-1:
            resultado = resultado[:-1]
            resultado += "}"
    return resultado

#Datos del enunciado
A="{1,2,3,4,5,6,7,10}"
B="{8,9,10,11}"

print(UnionConjuntos(A,B))