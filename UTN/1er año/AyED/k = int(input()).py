def eleerre(lr):
    lr = lr.split()
    l = int(lr[0])
    r = int(lr[1])
    return l, r

k = int(input())
lr = input()
l, r = eleerre(lr)

cadena = ""
num_mayor = 0

for i in range(l, r + 1):
    cadena += str(i)

for i in range(len(cadena) - k + 1):
    num = int(cadena[i:i+k])
    if num > num_mayor:
        num_mayor = num

print(num_mayor)