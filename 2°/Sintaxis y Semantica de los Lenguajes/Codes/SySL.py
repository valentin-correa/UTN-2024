def ejercicio_2():
    alfabeto = ["a","b","c","d","e","f","g"]
    cadena = str(input())
    x = 0
    for elemento in cadena:
        if elemento not in alfabeto:
            x = 1
    if x == 1:
        print("No es posible generar esta cadena a partir del alfabeto")
    else:
        print("Es posible generar esta cadena a partir del alfabeto")

def ejercicio_3():



print(ejercicio_2())    