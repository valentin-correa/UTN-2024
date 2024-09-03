datos = ""
while datos != "0 0":
    datos = ""
    contrato = ""
    output = ""

    datos += str(input())

    if datos == "0 0":
        break
    num = datos[0]

    for i in range(2, len(datos)):
        contrato += datos[i]
    for i in range(len(contrato)):
        if contrato[i] != num:
            output += contrato[i]
    
    if output == "":
        print(0)
    elif int(output) + 1 == 1:
        print(0)
    else:
        print(int(output))