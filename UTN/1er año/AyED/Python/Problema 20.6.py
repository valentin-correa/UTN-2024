productos = str(input("Ingrese los productos en la cesta de compras separados por una coma: "))
cad_productos = ""
productos += " "
for i in range(len(productos)):
    if productos[i] != "," and productos[i] != " ":
        cad_productos += productos[i]
    else:
        if cad_productos != "":
            print(cad_productos)
        cad_productos = ""