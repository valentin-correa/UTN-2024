def transformador_binario(sistema_1, num):
    if sistema_1 == "binario":
        return num
    if sistema_1 == "decimal":
        num = int(num, 10)
    if sistema_1 == "hexadecimal":
        num = int(num, 16)
    if sistema_1 == "octal":
        num = int(num, 8) 
    if num == 0:
        return 0
    binario = ""
    while num > 0:
        num_str = num%2 
        binario = str(num_str) + binario
        num = num // 2
    return binario

def transformador_decimal(num):
    if sistema_1 != "binario" and sistema_1 != "decimal" and sistema_2 != "octal":
        num = transformador_binario(sistema_1, num)
    ac = int()
    if str(num):
        num = num[::-1]
        for i in range(len(num)):
            ac += int(num[i]) * 2 ** i

        return str(ac)

def transformador_hexa(num):
    if sistema_1 != "binario":
        num = transformador_binario(sistema_1, num)
    ceros = "0"
    num_hexa = ""
    num_bin_hexa = ""
    for i in range(len(num)):
        if len(num) % 4 != 0:
           num = ceros + num
        else:
           break
       
    for i in range(0, len(num), 4):
            num_bin_hexa += num[i:i+4]
            num_hexa += conversor_hexa(num_bin_hexa)
            num_bin_hexa = ""

    return num_hexa

def transformador_octal(num):
    if sistema_1 != "binario":
        num = transformador_binario(sistema_1, num)
    ceros = "0"
    num_octa = ""
    num_bin_octa = ""
    for i in range(len(num)):
        if len(num) % 3 != 0:
           num = ceros + num
        else:
           break 
    for i in range(0, len(num), 3):
            num_bin_octa += num[i:i+3]
            num_octa += transformador_decimal(num_bin_octa)
            num_bin_octa = ""

    return num_octa

def conversor_hexa(num_bin_hexa):
    if int(num_bin_hexa, 2) < 10:
        num_bin_hexa = transformador_decimal(num_bin_hexa)
    if num_bin_hexa == "1010":
        num_bin_hexa = "A"
    if num_bin_hexa == "1011":
        num_bin_hexa = "B"
    if num_bin_hexa == "1100":
        num_bin_hexa = "C"
    if num_bin_hexa == "1101":
        num_bin_hexa = "D"
    if num_bin_hexa == "1110":
        num_bin_hexa = "E"
    if num_bin_hexa == "1111":
        num_bin_hexa = "F"

    return num_bin_hexa

def calculadora(sistema_2):
    if sistema_2 == "decimal":
        return print(transformador_decimal(num))
    if sistema_2 == "binario":
        return print(transformador_binario(sistema_1, num))
    if sistema_2 == "hexadecimal":
        return print(transformador_hexa(num))
    if sistema_2 == "octal":
        return print(transformador_octal(num))    

sistema_1 = str(input("Ingrese un sistema : "))
sistema_2 = str(input("Ingrese otro sistema: "))
num = str(input("Ingrese el número: "))
calculadora(sistema_2)
