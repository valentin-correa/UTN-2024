def cambio(leds, cambios, leds_bien):
    x = bool
    for i in range(int(cambios)):
        if leds_bien != []:
            leds = [fila[:] for fila in leds_bien]
        if i == 0:
            if leds[0] == "O":
                leds_bien.append("X")
            else:
                leds_bien.append("O")
        else:
            leds_bien = []
            if leds[0] == "O":
                leds_bien.append("X")
                x = True
            else:
                leds_bien.append("O")
                x = True
        for j in range(len(leds_bien), len(leds), 1):
            if leds_bien[j - 1] == "X" and x == True:
                x = True
                if leds[j] == "X":
                    leds_bien.append("O")
                else:
                    leds_bien.append("X")
            else:
                x = False
                leds_bien.append(leds[j]) 
    return leds_bien

num = int(input())

for i in range(num):
    cadena = str(input())
    leds = []
    leds_bien = []
    cambios = ""
    x = False
    for j in range(len(cadena)):
        if x == False:
            if cadena[j] != " " and x == False:
                leds.append(cadena[j])
            else:
                x = True    
        else:
            cambios += cadena[j]
    print(cambio(leds, cambios, leds_bien))
    

    
    
