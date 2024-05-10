#def ingrearMatriz():
#    vertices=int(input("Ingresar cantidad de vertices de la relacion"))
#    matriz=[[int() for filas in range(vertices)]for columnas in range(vertices)]
#    for i in range(vertices):
        
def PropiedadReflexiva(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j:
                if matriz[i][j]!=1:
                    print("Las relacion agregada es: [",i+1,",",j+1,"]")
                matriz[i][j]=1
    return matriz



def DetectorPropiedadIrreflexiva(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j and matriz[i][j]==1:
                return "No es irreflexiva"
    return "Es irreflexiva"



def PropiedadSimetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i!=j and matriz[i][j]==1 or matriz[j][i]==1:
                matriz[i][j]==1
                matriz[j][i]==1
    return matriz



def PropiedadTransitiva(matriz):
    for k in range(len(matriz)):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz[i][j]=matriz[i][j] or (matriz[i][k] and matriz[k][j])
    return matriz



def MatrizDeConectividad(matriz):
    for k in range(len(matriz)):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz[i][j]=matriz[i][j] or (matriz[i][k] and matriz[k][j])
    return matriz



def MatrizDeAlcanzabilidad(matriz):
    for k in range(len(matriz)):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz[i][j]=matriz[i][j] or (matriz[i][k] and matriz[k][j])
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j:
                matriz[i][j]=1
    return matriz

matriz = [[0,0,1],[1,0,0],[0,0,1]]  
print(DetectorPropiedadIrreflexiva(matriz))