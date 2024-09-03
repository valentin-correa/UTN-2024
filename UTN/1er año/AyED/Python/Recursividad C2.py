def C(n):
    if n == 0:
        return -1
    if n == 1:
        return 2
    else:
        return (C(n-1) * C(n-2) ** 3)
    
n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
    print(C(i))