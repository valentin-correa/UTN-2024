def orden_alfabetico(cadena):
    alfabeto="abcdefghijklmnñopqrstuvwxyz"
    vector_posicion=[int() for i in range(len(cadena))]
    cadena_nueva=""
    for j in range(len(cadena)):
        i=0
        while i !=len(alfabeto):
            if alfabeto[i]==cadena[j]:
                vector_posicion[j]=i
                break
            i+=1
    
    vector_posicion.sort()
    for i in range(len(cadena)):
        cadena_nueva+=alfabeto[vector_posicion[i]]

    return cadena_nueva

def cant_voc(cadena):
    cadena_ordenada = ""
    cadena_pas = ""
    cadena += " "
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_pas += cadena[i]
        else:
            cadena_ordenada += orden_alfabetico(cadena_pas) + " "
            cadena_pas = ""
        
    return cadena_ordenada

cadena = str(input())
print(cant_voc(cadena))