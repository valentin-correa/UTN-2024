def EjercicioA(cad, p1, p2, p3):
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(cad) - 2):
        aux = cad[i:i+3]
        if p1 == aux:
            c1 += 1
        elif p2 == aux:
            c2 += 1
        elif p3 == aux:
            c3 += 1
    return c1, c2, c3

def EjercicioB(cad, p1, p2, p3):
    c1 = []
    c2 = []
    c3 = []
    for i in range(len(cad) - 2):
        aux = cad[i:i+3]
        if p1 == aux:
            c1 += str(i)
        elif p2 == aux:
            c2 += str(i)
        elif p3 == aux:
            c3 += str(i)
    return c1, c2, c3

B = {"0", "1"}
cad = "010110101110"
p1 = "101"
p2 = "111"
p3 = "010"

print(EjercicioA(cad, p1, p2, p3))
print(EjercicioB(cad, p1, p2, p3))