A = {"1","2","3","a","b","c","x", "y", "z"}
cadenas = ["1acxz","2ybc1za","11y2abx"]
x = bool

for elementos in cadenas:
    for i in elementos:
        if i in A:
            x = True
        else:
            x = False