def C(n):
    if n in {0, 1}:
      return n + 2
    else:
        return (2*C(n-1) / C(n-2)) + C(n-1)
    
n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
    print(C(i))