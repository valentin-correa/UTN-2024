'''
2- INTERSECCIÓN DE CONJUNTOS
Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la intersección de estos conjuntos será A∩B={4,5}
'''
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

def interseccionConjuntos(A,B):
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

    #Pasar solo los repetidos a una lista
    conjuntoSinRepetidos = []
    conjuntoRepetidos = []

    for i in conjunto:
        if i not in conjuntoSinRepetidos:
            conjuntoSinRepetidos.append(i)
        else:
            conjuntoRepetidos.append(i)
    
    #Lo formateo para imprimirlo en pantalla
    resultado = "{"

    VAR = len(conjuntoRepetidos)
    for i in range(VAR):    
        resultado += str(conjuntoRepetidos[i]) + ","
        if i == len(conjuntoRepetidos)-1:
            resultado = resultado[:-1]
            resultado += "}"

    return resultado
#Datos del problema
A="{1,2,3,4,5}"
B="{4,5,6,7,8,9}"

print(interseccionConjuntos(A,B))