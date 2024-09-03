def calcular_binario(num):
    if num == 0:
        return 0
    binario = ""
    while num > 0:
        num_str = num%2 
        binario = str(num_str) + binario
        num = num // 2
    return binario
num = int(input("Ingrese un número: "))
print(calcular_binario(num))