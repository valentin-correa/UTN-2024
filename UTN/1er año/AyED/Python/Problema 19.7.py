def subcad(cadena1, cadena2):
   checker = ""
   x = False
   for i in range(len(cadena1)):
      if cadena1[i] == cadena2[0]:
        x = True
      if x == True:
        checker += cadena1[i]
      if cadena1[i] == " ":
        x = False
      if checker == cadena2:
        print("La segunda cadena es una subcadena de la primera")
      if cadena1[i-1] == " " and x == False:
        checker = ""
    
def abc(cadena):
    ac = int()
    ac2 = int()
    cadena_1 = ""
    checker = ""
    cadena_abc = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(cadena)):
        if i == 0 or cadena[i-1] == " ":
            checker += cadena[i]
        for i in range(cadena_abc):
            if checker == cadena_abc[i]:
               ac += i
            if checker == cadena_abc[i]:
               cadena_1 += i
               break
        
        checker = ""
        if cadena[i-1] == " ":
            checker += cadena[i]
        for i in range(cadena_abc):
            if checker == cadena_abc[i]:
               ac2 += i
               break
    
        if ac < ac2:
           print()

cadena1 = str(input("Ingrese una cadena: "))
cadena2 = str(input("Ingrese otra cadena: "))
(subcad(cadena1, cadena2))
