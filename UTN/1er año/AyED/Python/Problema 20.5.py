fecha = str(input("Ingrese su fecha de nacimiento (dd/mm/aaaa): "))
barra = 0
dia = ""
mes1 = ""
año = ""
for i in range(len(fecha)):
    if fecha[i] == "/":
        barra += 1
    if barra == 0 and fecha[i] != "/":
        dia += fecha[i]
    if barra == 1 and fecha[i] != "/":
        mes1 += fecha[i]
    if barra == 2 and fecha[i] != "/":
        año += fecha[i] 

dia = int(dia)
if mes1 == "01" or mes1 == "1":
    mes2 = "enero"
if mes1 == "02" or mes1 == "2":
    mes2 = "febrero"
if mes1 == "03" or mes1 == "3":
    mes2 = "marzo"
if mes1 == "04" or mes1 == "4":
    mes2 = "abril"
if mes1 == "05" or mes1 == "5":
    mes2 = "mayo"
if mes1 == "06" or mes1 == "6":
    mes2 = "junio"
if mes1 == "07" or mes1 == "7":
    mes2 = "julio"
if mes1 == "08" or mes1 == "8":
    mes2 = "agosto"
if mes1 == "09" or mes1 == "9":
    mes2 = "septiembre"
if mes1 == "10":
    mes2 = "octubre"
if mes1 == "11":
    mes2 = "noviembre"
if mes1 == "12":
    mes2 = "diciembre"

print(dia , "de", mes2 , "del", año)