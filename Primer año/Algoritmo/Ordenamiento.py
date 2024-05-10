def OrdenBurbuja(vector):
    aux=int()
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i]<vector[j]:
                aux=vector[j]
                vector[j]=vector[i]
                vector[i]=aux
    print(vector)

def OrdenSeleccion(vector):
    for i in range(0, len(vector)-1):
        menor=i
        for j in range(i+1, len(vector)):
            if vector[menor]>vector[j]:
                menor=j
        valormenor=vector[i]
        vector[i]=vector[menor]
        vector[menor]=valormenor
    print(vector)

def OrdenInserccion(vector):
    for j in range(len(vector)):
        actual=vector[j]
        i=j-1
        while i>=0 and vector[i]>actual:
            vector[i+1]=vector[i]
            i-=1
        vector[i+1]=actual
    print(vector)

def QuickSort(vector):
    pivote=vector[len(vector)/2]
    menor=0
    mayor=len(vector)
    for i in range(len(vector)):
        if vector[menor]>pivote:
            menor+=1
        elif vector[mayor]<pivote:
            mayor-=1
        elif vector

VectorDesorden=[42, 57, 14, 40, 96 , 19, 8, 68]
#OrdenBurbuja(VectorDesorden)
#OrdenSeleccion(VectorDesorden)
#OrdenInserccion(VectorDesorden)