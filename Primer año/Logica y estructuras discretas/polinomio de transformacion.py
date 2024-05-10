def Polinomio_de_transformacion(num, base):
    ac=int()
    num=str(num)
    num = num[::-1]
    for i in range(len(num)):
        ac+=int(num[i])*base**i
    return ac

print(Polinomio_de_transformacion(654, 8))