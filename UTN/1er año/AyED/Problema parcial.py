def eleerre(lr, l, r):
    x = False
    for i in range(len(lr)):
        if lr[i] == " ":
            x = True
        if x == False:
            l += lr[i]
        elif x == True and lr[i] != " ":
            r += lr[i]

    l = int(l)
    r = int(r)
    r -= l
    l -= 1
    return l, r
        
k = int(input())
lr = str(input())
l = ""
r = ""
cadena = ""
cadena2 = 0
num_mayor = 0
x = False

l, r = eleerre(lr, l, r) #Calculo L y R
aux = l

for i in range(r + 1):
    if len(cadena) <= r:
        aux += 1
        cadena += str(aux)
    else:
        break
cadena = cadena[0:r + 1]

for i in range(len(cadena) - 1):
    cadena2 = int(cadena[i:i+k])
    if cadena2 > num_mayor:
        num_mayor = cadena2

print(num_mayor)