def numero(cantidad):
    for i in range(cantidad):
        cantidad_de_leds=0
        numero=str(input())
        for j in range(len(numero)):
            if "1"==numero[j]:
                cantidad_de_leds+=2
            if "2"==numero[j]:
                cantidad_de_leds+=5
            if "3"==numero[j]:
                cantidad_de_leds+=5
            if "4"==numero[j]:
                cantidad_de_leds+=4
            if "5"==numero[j]:
                cantidad_de_leds+=5
            if "6"==numero[j]:
                cantidad_de_leds+=6
            if "7"==numero[j]:
                cantidad_de_leds+=3
            if "8"==numero[j]:
                cantidad_de_leds+=7
            if "9"==numero[j]:
                cantidad_de_leds+=6
            if "0"==numero[j]:
                cantidad_de_leds+=6
        print(cantidad_de_leds,"leds")
cantidad=int(input())
numero(cantidad)
