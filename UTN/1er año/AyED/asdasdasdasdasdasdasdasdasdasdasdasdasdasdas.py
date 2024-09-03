k = int(input())
l, r = map(int, input().split())
cadena = ""
cadena2 = 0
num_mayor = 0
x = False
aux = l
r -= l

for i in range(r):
    if len(cadena) < r:
        aux += 1
        cadena += str(aux)
    else:
        break
cadena = cadena[0:r]

for i in range(len(cadena) - 1):
    cadena2 = int(cadena[i:i+k])
    if cadena2 > num_mayor:
        num_mayor = cadena2

print(num_mayor)