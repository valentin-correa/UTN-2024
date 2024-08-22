def append(L1, L2, alfabeto):
    combinacion = L1 + "," + L2 + ","
    aux = ""
    for i in range(len(combinacion)):
        if combinacion[i] not in {"{", "}"}:
            if combinacion[i] != ",":
                aux += combinacion[i]
            else:
                alfabeto.append(aux)
                aux = ""
    return alfabeto

L1 = str(input())
L2 = str(input())
pal = str(input())
alfabeto = []
combinacion = (append(L1, L2, alfabeto))
x = bool

for i in range (len(pal)):
    for j in range (len(combinacion)):
        if pal[i] == combinacion[j]:
            x = True
            break
        else:
            x = False
    if x == False:
        print("No")
        break
if x == True:
    print("Si")
