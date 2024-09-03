def cambio(leds, leds_bien, cambios):
    x = bool
    for i in range(int(cambios)):
        if leds_bien != "":
            leds = leds_bien
        if i == 0:
            if leds[0] == "O":
                leds_bien += "X"
            else:
                leds_bien += "O"
        else:
            leds_bien = ""
            if leds[0] == "O":
                leds_bien += "X"
                x = True
            else:
                leds_bien += "O"
                x = True
    
        for j in range(len(leds_bien), len(leds), 1):
            if leds_bien[j - 1] == "X" and x == True:
                x = True
                if leds[j] == "X":
                    leds_bien += "O"
                else:
                    leds_bien += "X"
            else:
                x = False
                leds_bien += leds[j] 
    outputs.append(leds_bien)

    return outputs

num = int(input())
outputs = []

for i in range(num):
    cadena = str(input())
    cadena += " "
    leds_bien = ""
    leds = ""
    cambios = ""
    espacios = 0

    for i in range(len(cadena)):
        if cadena[i] == " ":
            espacios += 1
        else:
            if espacios == 0:
                leds += cadena[i]
            elif espacios == 1:
                cambios += cadena[i]
            else:
                break
    cambio(leds, leds_bien, cambios)

for i in range(len(outputs)):
    print(outputs[i])
        
    