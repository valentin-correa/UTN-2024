def QuickSort(vector, inicio, final):
    pivote=len(vector)-1
    PunteroMenor=0
    PunteroMayor=len(vector)-1
    for i in range(inicio,final):
        if vector[PunteroMenor]<vector[pivote]:
            PunteroMenor+=1
        elif vector[PunteroMayor]>vector[pivote]:
            PunteroMayor-=1
        else: 
            Aux=vector[PunteroMayor]
            vector[PunteroMayor]=vector[PunteroMenor]
            vector[PunteroMenor]=Aux
    return vector
#QuickSort(vector, PunteroMenor, pivote)
        
def quicksort(array, ini, fin): #  Define la función usando el vector, el primer elemento y el último.
    if ini < fin: #El índice del primer elemento es menor al índice del último elemento del vector a analizar. [SI SON IGUALES NO HACE NADA]
        pivot = division (array, ini, fin) #Define al pivot en base a la otra función (seguir)
        quicksort(array, ini, pivot - 1) #Hace quicksort con desde el principio del vector hasta antes del pivot
        quicksort(array, pivot + 1, fin) #Hace quicksort desde el pivot hasta el final del vector.
        



def division(array, ini, fin): #Define la función usando el vector original, el desde y el hasta dado por la función quicksort.
    i = ini #Define que i sea igual al inicio de la nueva sorteada.
    j = fin - 1 #Define que j sea igual al penúltimo elemento de la nueva sorteada.
    pivot = array[fin] #Define al pivot como el último elemento de la nueva sorteada.
    while i < j: #Mientras que el inicio de la nueva sorteada no llegué al final de la nueva sorteada.
        while i < fin and array[i] < pivot: #Mientras que el inicio de la nueva sorteada sea menor al final del vector nueva sorteada Y el vector en donde esté i sea menor al pivot.
            i+=1 #Mueve el puntero izquierdo hacia la derecha
        
        while j > ini and array[j] >= pivot: #Mientras el puntero derecho sea mayor al inicio de la nueva sorteada Y el vector en donde esté el puntero derecho sea mayor o igual al pivot.
            j-=1 #Mueve el puntero derecho hacia la izquierda.

        if i < j: #Si donde está el puntero izquierdo es menor a donde está el puntero derecho.
            array[i], array[j] = array[j], array[i] #Intercambia el valor del puntero izquierdo con el valor del puntero derecho.
    
    if array[i] > pivot: #Si el valor donde está el puntero izquierdo es mayor al pivot (que siempre está al final)
        array[i], array[fin] = array[fin], array[i] #Intercambia el valor del puntero izquierdo con el valor que está al final (pivot)

    return i #Retorna el índice del pivot.

VectorDesorden=[42, 57, 14, 40, 96, 19, 8, 68]
print(QuickSort(VectorDesorden, 0, 7))

