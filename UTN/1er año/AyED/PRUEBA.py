verts = int(input())
matriz = []

for i in range(verts):
    fila = [int(x) for x in input().split()]
    matriz.append(fila)

for k in range(verts):
        for i in range(verts):
            for j in range(verts):
                matriz[i][j] = matriz[i][j] or (matriz[i][k] and matriz[k][j])

print("")
for i in range(verts):
    print(" ".join(map(str, matriz[i])))
    