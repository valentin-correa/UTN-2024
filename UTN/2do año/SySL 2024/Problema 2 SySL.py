import random

def combinar(cadena):
    subcadenas = []
    
    for i in range(len(cadena)):
        for j in range(i + 1, len(cadena) + 1):
            subcadenas.append(cadena[i:j])
    return subcadenas

def EjercicioA(cadenas, combinaciones):
    for cadena in cadenas:
        subcadenas = combinar(cadena)
        for elemento in subcadenas:
            if elemento not in combinaciones:
                combinaciones.append(elemento)
    return combinaciones

def EjercicioB(combinaciones):
    for elemento in combinaciones:
        cad1 = combinaciones[random.randint(0, len(combinaciones) - 1)]
        cad2 = combinaciones[random.randint(0, len(combinaciones) - 1)]
    cad3 = cad1 + cad2
    cad4 = cad1[::-1]
    return cad3, cad4
        
def EjercicioC():
    

A = {"1", "2", "3", "a", "b", "c", "x", "y", "z"}
cadenas = ["1acxz", "2ybc1za", "11y2abx"]
combinaciones = []
print(EjercicioA(cadenas, combinaciones))
combinaciones = EjercicioA(cadenas, combinaciones)
print(EjercicioB(combinaciones))