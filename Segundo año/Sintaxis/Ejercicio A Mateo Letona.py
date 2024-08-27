cadena = []
algo = ""
alfabetoString = "{a,b,c,d,e,f,g}"

def splitDeConjuntos(alfabetoString):
  alfabetoString = alfabetoString[1:]
  alfabetoString = alfabetoString[:len(alfabetoString)-1]
  alfabeto = alfabetoString.split(",")
  return alfabeto

def Ejercicio_A(alfabetoString):
  alfabeto = splitDeConjuntos(alfabetoString)

  for i in alfabeto:
      for j in alfabeto:
          for k in alfabeto:
              for l in alfabeto:
                  algo = i+j+k+l
                  cadena.append(algo)
  return cadena


print(Ejercicio_A(alfabetoString))