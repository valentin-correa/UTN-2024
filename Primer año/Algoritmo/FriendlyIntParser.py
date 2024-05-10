def aaa():
    text2=""
    text=str(input())
    for i in range(len(text)):
        if text[i] not in {" ",".",","}:
            if text[i] in {"a","b","c","d","e","f","g","h","i","j","k","m","n","p","q","r","s","t","x","y","z","w","v"}:
                return "error"
            if text[i]=="o" or text[i]=="O":
                text2+="0"
            if text[i]=="l":
                text2+="1"
            if text[i] not in {"o","O","l"}:
                text2+=text[i]
    if text2=="":
        return "error"
    if text==None or ValueError:
        return "error"
    if int(text2)>2147483647:
        return "error"
    else:
        return int(text2)

while True:
    try:
        print(aaa())
    except EOFError:
        break