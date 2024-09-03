def transformador_reflexiva(matriz, verts):
    for i in range(verts):
        for j in range(verts):
            if i == j:
                matriz[i][j] = 1
    return matriz

def transformador_irreflexiva(matriz, verts):
    for filas in range(verts):
        for columnas in range(verts):
            if filas == columnas:
                matriz[filas][columnas] = 0
    return matriz

def transformador_transitiva(matriz, verts):
    for k in range(verts):
        for i in range(verts):
            for j in range(verts):
                matriz[i][j] = matriz[i][j] or (matriz[i][k] and matriz[k][j])
    return matriz

def transformador_simetrica(matriz, verts):
    for i in range(verts):
        for j in range(verts):
            if i != j and (matriz[i][j] == 1 or matriz[j][i] == 1):
                matriz[i][j] = 1
                matriz[j][i] = 1
    return matriz

def detector_simetrica(matriz, verts):
    mat_aux = [fila[:] for fila in matriz]
    matriz = transformador_simetrica(matriz, verts)
    if mat_aux == matriz:
        x = True
        print("La relación es simetrica")
    else:
        x = False
        print("La relación NO es simetrica")
    return x

def detector_transitiva(matriz, verts):
    mat_aux = [fila[:] for fila in matriz]
    matriz = transformador_transitiva(matriz, verts)
    if mat_aux == matriz:
        x = True
        print("La relación es transitiva")
    else:
        x = False
        print("La relación NO es transitiva")
    return x

def detector_reflexiva(matriz, verts):
    x = True
    for i in range(verts):
        if x == False:
            break
        for j in range(verts):
            if i == j:
                if matriz[i][j] != 1:
                    print("No es reflexiva")
                    x = False
                    break
    if x == True:
        print ("Es reflexiva")
    return x

def detector_irreflexiva(matriz):
    x = True
    for filas in range(3):
        if x == False:
            break
        for columnas in range(3):
            if filas == columnas and matriz[filas][columnas] != "0":
                print("No es irreflexiva")
                x = False
                break
    if x == True:
        print ("Es irreflexiva")

def detector_Equivalencia(matriz, verts):
    x = bool # NO FUNCIONA NO USAR
    detector_reflexiva(matriz, verts)
    if x == True:
        detector_simetrica(matriz, verts)
        if x == True:
            detector_transitiva(matriz, verts)
            if x == True:
                print("La relación es de equivalencia")
    else:
        print("La relación NO es de equivalencia")


verts = int(input("Ingrese el número de vértices: "))
matriz = []

for i in range(verts):
    fila = [int(x) for x in input().split()]
    matriz.append(fila)

print("Matriz inicial")
for i in range(verts):
        print(matriz[i])

detector_Equivalencia(matriz, verts)
