def conversor_hexa(num_str):
    if num_str < 10:
        num_str = num_str
    num_str = str(num_str)
    if num_str == "10":
        num_str = str("A")
    if num_str == "11":
        num_str = str("B")
    if num_str == "12":
        num_str = str("C")
    if num_str == "13":
        num_str = str("D")
    if num_str == "14":
        num_str = str("E")
    if num_str == "15":
        num_str = str("F")
    return num_str    

def hexa_decimal(num):
    ac = 0
    for i in range(len(num)):
        if num[i] == "F":
            ac += int(15)
        if num[i] == "E":
            ac += int(14)
        if num[i] == "D":
            ac += int(13)
        if num[i] == "C":
            ac += int(12)
        if num[i] == "B":
            ac += int(11)
        if num[i] == "A":
            ac += int(10)

    return ac

def tranformador_decimal(sistema_1, num):
    if sistema_1 == 16:
        num = hexa_decimal(num)
        return num
    num = str(num)
    num = num[::-1]
    ac=0
    for i in range(len(num)):
        ac += int(num[i]) * sistema_1 ** i

    return str(ac)

def decimal_binario(num):
    num=int(num)
    binario=""
    while num > 0:
        num_str = num % 2 
        binario = str(num_str) + binario
        num = num // 2
    return binario

def decimal_hexa(num):
    num=int(num)
    hexa=""
    while num > 0:
        num_str = num % 16
        hexa = conversor_hexa(num_str) + hexa
        num = num // 16
    return hexa

def decimal_octa(num):
    num=int(num)
    octal=""
    while num > 0:
        num_str = num % 8 
        octal = str(num_str) + octal
        num = num // 8
    return octal

def calculadora(sistema_1, sistema_2):
    if sistema_1 == "decimal":
        sistema_1 = int(10)
    if sistema_1 == "binario":
        sistema_1 = int(2)    
    if sistema_1 == "hexadecimal":
        sistema_1 = int(16)
    if sistema_1 == "octal":
        sistema_1 = int(8)
    if sistema_2 == "decimal":
        return print(tranformador_decimal(sistema_1, num))
    if sistema_2 == "binario":
        return print(decimal_binario(tranformador_decimal(sistema_1, num)))
    if sistema_2 == "hexadecimal":
        return print(decimal_hexa(tranformador_decimal(sistema_1, num)))
    if sistema_2 == "octal":
        return print(decimal_octa(tranformador_decimal(sistema_1, num)))  
    
sistema_1 = str(input("Ingrese un sistema : "))
sistema_2 = str(input("Ingrese otro sistema: "))
num = str(input("Ingrese el número: ")) 
calculadora(sistema_1, sistema_2)