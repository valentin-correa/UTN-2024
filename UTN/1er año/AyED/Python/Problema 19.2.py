def car2(cadena):
    for i in range(2):
        print(cadena[i], end="")

def car2_Rev(cadena):
    cadena_rev=""
    cadena = cadena[::-1]
    for i in range(3):
        cadena_rev += cadena[i]

    cadena_rev = cadena_rev[::-1]
    print(cadena_rev)    

def carcad2(cadena):
    cadena_3=""
    for i in range(len(cadena)):
        if i%2 == 0:
            cadena_3 += cadena[i]

    print(cadena_3)     

def cad_Rev(cadena):
    print(cadena[::-1])

def mirror(cadena):
    print(cadena + cadena[::-1])

cadena=str(input("Ingrese una oración: "))
car2(cadena)
car2_Rev(cadena)
carcad2(cadena)
cad_Rev(cadena)
mirror(cadena)