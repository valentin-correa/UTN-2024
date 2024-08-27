def palindromo(cadena1,cadena2): #Ingresan dos palabras y determinar si una es la inversa de la otra
    palindromo = False
    if len(cadena1)==len(cadena2):
        for i in range(len(cadena1)):
            if cadena1[i:i+1] != cadena2[len(cadena2)-i-1:len(cadena2)-i]:
                palindromo = False
                break
            else:
                palindromo = True
    return palindromo


def ocurrencia(cadena,sim): #Ingresa una palabra y determinar el número de ocurrencias de un símbolo dado.

    ac = 0
    for i in range(len(cadena)):
        if cadena[i:i+1] == sim:
            ac = ac + 1
    return ac

'''
Dado un alfabeto, determinar si las palabras ingresadas, están
formadas por dicho alfabeto (mostrar mensaje OK o NO OK, según el
caso) . En el caso de contener otros elementos que no pertenezcan al
alfabeto, mostrar cuales son los elementos diferentes.
'''
def splitDeConjuntos(alfabetoString): # Elimina las llaves del inicio y el final del alfabeto
  alfabetoString = alfabetoString[1:]
  alfabetoString = alfabetoString[:len(alfabetoString)-1]
  return alfabetoString

def ocurrenciaCadena(alfabeto,cadena): # Verifica que la cadena este compuesta por simbolos dentro del alfabeto LOS SIMBOLOS NO PUEDEN SER DE MAS DE UN CARACTER. 
                                       # La cadena se ingresa "aaaa" por ejemplo y el alfabeto "{a,b,c,d,e}"
    longitud = 0
    alfabeto = splitDeConjuntos(alfabeto)
    
    for i in range(len(alfabeto)):
       for j in range(len(cadena)):
            if alfabeto[i:i+1] != ",":
                if alfabeto[i:i+1] == cadena[j:j+1]:
                    longitud += 1
            else:
                break
    if longitud == len(cadena):

        return "La cadena esta compuesta por los simbolos del afabeto propuesto"
    else:
        return "La cadena no esta compuesta por los simbolos del afabeto propuesto"

def separar(cadena):
    resultado = ""
    listado = []
    ac = 0

    cadena = cadena[:len(cadena)-1]
    cadena = cadena[1:len(cadena)]
    for i in range(len(cadena)):
        if cadena[i] != ",":
            resultado = resultado + cadena[i]
        else:
            ac += 1
            listado.append(resultado)

def alf4(L1,L2,cadena):
    alf = L1 + L2
    malos = ""
    check = False
    for i in range(len(alf)):

        for j in range(len(cadena)):
            if cadena[j:j+1] == alf[i:i+1] and cadena[j:j+1] != "{" and cadena[j:j+1] != "}" and cadena[j:j+1] != "," and alf[i:i+1] != "{"and alf[i:i+1] != "}"and alf[i:i+1] != ",":
                check = True
            else:
                malos = malos + cadena[j:j+1]


    return malos

def ocurrenciaCadenaSim(alfabeto,cadena): # Verifica que la cadena este compuesta por simbolos dentro del alfabeto LOS SIMBOLOS PUEDEN SER DE MAS DE UN CARACTER. 
                                            # La cadena se ingresa "aaaa" por ejemplo y el alfabeto "{ab,cd,e}"
    alfabeto = listarAlfabeto(alfabeto)
    acierto = True
    
    for i in range(len(alfabeto)):
        for j in range(len(cadena)):
            if alfabeto[i] not in cadena and acierto == True :
                acierto = False # Cuando sea false significa que no es una palbra valida
            else:
                
    if acierto == False:
        return "No es una palabra valida"
    return 


def listarAlfabeto(alfabeto): # Lista todos los simbolos de un alfabeto en una lista
    alfabeto = splitDeConjuntos(alfabeto)
    listaAlfabeto = [] 
    cadAux = ""
    
    for i in range(len(alfabeto)):
        if alfabeto[i:i+1] != ",":
            cadAux += alfabeto[i:i+1]
        else:
            listaAlfabeto.append(cadAux)
            cadAux = ""
        if i == len(alfabeto)-1:
            listaAlfabeto.append(cadAux)
    
    return listaAlfabeto
    
alfabeto = "{ho,la,mu,n,do}"

#cadena1 = input()
#cadena2 = input()
#cadena3 = input()
#sim = input()
#print(palindromo(cadena1,cadena2))
#print(ocurrencia(cadena3,sim))
print(ocurrenciaCadenaSim(alfabeto,"hola mundo"))