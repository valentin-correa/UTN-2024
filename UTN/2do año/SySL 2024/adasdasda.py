def generar_subcadenas(cadena):
    subcadenas = []
    
    for i in range(len(cadena)):
        for j in range(i + 1, len(cadena) + 1):
            subcadenas.append(cadena[i:j])
    return subcadenas

A = {"1", "2", "3", "a", "b", "c", "x", "y", "z"}
cadenas = ["1acxz", "2ybc1za", "11y2abx"]
combinaciones = []

for cadena in cadenas:
    subcadenas = generar_subcadenas(cadena)
    for elemento in subcadenas:
        if elemento not in combinaciones:
            combinaciones.append(elemento)
print(combinaciones)