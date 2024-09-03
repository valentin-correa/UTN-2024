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

def interseccion(A, B): #Función para calcular la union entre los conjuntos "A" y "B"
    resultado = [] #Lista o vector donde se encontrará el conjunto resultante de la intersección de "A" y "B"
    for elemento in A:
        if elemento in B: #Si el elemento de "A" se encuentra en el conjunto "B" entra en la condición
            resultado.append(elemento)  
    return resultado #Conjunto resultante de la intersección de "A" y "B"

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

print(interseccion(A, B)) #Mostramos el conjunto resultante