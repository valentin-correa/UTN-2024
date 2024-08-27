'''
Ejercicio C:
Modificar el algoritmo para generar cadenas que cumplan las siguientes reglas adicionales:
- Informar si existen repeticiones consecutivas del mismo símbolo en la cadena
ingresada
- Informar aquellas cadenas que contengan una subcadena {ab, cd, ef}.
'''
subcadena = "{ab,cd,ef}"
cadena = []
algo = ""
alfabetoString = "{a,b,c,d,e,f,g}"

def splitDeConjuntos(alfabetoString):
    alfabetoString = alfabetoString[1:]
    alfabetoString = alfabetoString[:len(alfabetoString)-1]
    #alfabeto = alfabetoString.split(",")
    return alfabetoString

def Ejercicio_A(alfabetoString):
    alfabeto = splitDeConjuntos(alfabetoString)
    for i in range(len(alfabeto)):
        if alfabeto[i:i+1] != ",":
            for j in range(len(alfabeto)):
                if alfabeto[j:j+1] != ",":
                    for k in range(len(alfabeto)):
                        if alfabeto[k:k+1] != ",":
                            for l in range(len(alfabeto)):
                                if alfabeto[l:l+1] != ",":
                                    algo = alfabeto[i:i+1]+alfabeto[j:j+1]+alfabeto[k:k+1]+alfabeto[l:l+1]
                                    cadena.append(algo)
    print (cadena)
    return cadena

def Ejercicio_C(cadena):
    for i in range(len(cadena)):
        cadenaAnalisada = cadena[i]

        if cadenaAnalisada[0] == cadenaAnalisada[1] or cadenaAnalisada[1] == cadenaAnalisada[2] or cadenaAnalisada[2] == cadenaAnalisada[3]:
            print(cadenaAnalisada + " Tiene una repeticion")
        else:
            print(cadenaAnalisada + " No tiene una repeticion")

        if cadenaAnalisada[0:2] == "ab" or cadenaAnalisada[1:3] == "ab" or cadenaAnalisada[2:4] == "ab":
            print(cadenaAnalisada + " Tiene una suecuencia ab en alguna parte")
        if cadenaAnalisada[0:2] == "cd" or cadenaAnalisada[1:3] == "cd" or cadenaAnalisada[2:4] == "cd":
            print(cadenaAnalisada + " Tiene una secuencia cd en alguna parte")
        if cadenaAnalisada[0:2] == "ef" or cadenaAnalisada[1:3] == "ef" or cadenaAnalisada[2:4] == "ef":
            print(cadenaAnalisada + " Tiene una secuencia ef en alguna parte")
        
            
print(Ejercicio_C(Ejercicio_A(alfabetoString)))