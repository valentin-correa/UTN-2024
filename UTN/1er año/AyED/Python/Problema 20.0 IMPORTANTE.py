def Find(cadena1, cadena2):
   checker = ""
   pos = 0
   x = False
   for i in range(len(cadena1)):
      if cadena1[i] == cadena2[0]:
        x = True
      if x == True:
        checker += cadena1[i]
        if len(checker) < 2:
            pos += i        
      if cadena1[i] == " ":
        x = False
      if cadena1[i-1] == " " and x == False:
        checker = ""
      if checker == cadena2:
        return pos   

def index(cadena1, cadena2):
  cad_index = ""
  i = 0
  for j in range(len(cadena1)):
    while i < len(cadena1):  
      if cadena1[i] != " ":
        cad_index += cadena1[i]
        i += 1
      if cad_index == cadena2:
        return j
    

cadena1 = str(input("Ingrese una cadena: "))
cadena2 = str(input("Ingrese lo que quiere encontrar: "))
print(index(cadena1, cadena2))