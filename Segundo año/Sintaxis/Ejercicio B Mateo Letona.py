'''
Determinar si las siguientes cadenas son posibles de ser generadas por el alfabeto dado.
- abcg
- zdfc
- cfeg
- dflm
- gadc
- gasr
Ejemplo: Dado el alfabeto {0, 1} y la cadena "010", el algoritmo debería verificar que "010" es una
cadena válida de longitud 3.
'''
def splitDeConjuntos(alfabetoString):
  alfabetoString = alfabetoString[1:]
  alfabetoString = alfabetoString[:len(alfabetoString)-1]
  return alfabetoString


def Ejercicio_B(alfabeto,cadena):
    longitud = 0

    for i in range(len(alfabeto)):
       for j in range(len(cadena)):
            if alfabeto[i:i+1] != ",":
                if alfabeto[i:i+1] == cadena[j:j+1]:
                    longitud += 1
            else:
                break
    if longitud == len(cadena):

        return "Es valida de longitud " + str(longitud)
    else:
        return "No es valida"
#alfabeto = "{a,b,c,d,e,f,g}" Ejemplos
alfabeto = input() #Formato de Alfabeto

#cadena = "abcgaa1a" Ejemplos
cadena = input() #Formato de una palabra

print(Ejercicio_B(splitDeConjuntos(alfabeto),cadena))


