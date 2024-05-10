def numeros(entrada):
    cadena=""
    if entrada!=None:
        for k in range(len(entrada)):
            if entrada[k]=="O" or entrada[k]=="o":
                cadena+="0"
            elif entrada[k]=="l":
                cadena+="1"
            elif entrada[k] in {"0","1","2","3","4","5","6","7","8","9"}:
                cadena+=entrada[k]
            elif entrada[k] not in {","," "}:
                return "error"

    elif entrada==None or ValueError:
        return("error")

    if cadena!="":
        if int(cadena)>2147483647:
            return("error")
        else:
            return(int(cadena))
    else:
        return("error")
        
while True:
    try:
        ingreso = str(input())
        print(numeros(ingreso))
    except EOFError:
        break