def conjunto(L1, L2):
    combinacion = ""
    for i in range(len(L1)):
        if L1[i] not in {"{", "}"}:
            if L1[i] == ",":
                combinacion += " "
            else:
                combinacion += L1[i]
    combinacion += " "
    for i in range(len(L2)):
        if L2[i] not in {"{", "}"}:
            if L2[i] == ",":
                combinacion += " "
            else:
                combinacion += L2[i]
    return combinacion

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
print(combinacion)
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
