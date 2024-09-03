def split(string, array): #Función para obtener el conjunto en formato de lista o vector
    aux = ""
    i = 0
    while i < len(string):
        while string[i] not in {",", " "}: #Mientras no se esté leyendo un dato que no nos interesa se itera
            aux += string[i]
            i += 1 
        array.append(aux) #Se agrega el elemento al conjunto
        aux = ""
        i += 1
    return array #Conjunto final

def union(A, B): #Función para calcular la union entre los conjuntos "A" y "B"
    resultado = [] #Lista o vector donde se encontrará el conjunto resultante de la union de "A" y "B"
    for elemento in A:
        resultado.append(elemento) #Se agrega a resultado todo el conjunto "A"
    
    for elemento in B:
        if elemento not in resultado: #Si el elemento no se encuentra en el conjunto resultante, este se agrega al resultado de la unión, de esta manera evitamos la repetición de elementos
            resultado.append(elemento)
    return resultado #Conjunto resultante de la unión de "A" y "B"

string = str(input()) #Cadena con el conjunto 
string += " "
array = [] 
split(string, array) #Cadena con el conjunto 
A = array 
array = []
string = str(input())
string += " "
split(string, array)
B = array

print(union(A, B)) #Mostramos el conjunto resultante