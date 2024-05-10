def funcion(n):
    if n==0 or n==1:
        return n+2
    else:
        return 2*funcion(n-1)/funcion(n-2)+funcion(n-1)
def serie(n):
    for i in range(1,n+1):
        print(funcion_2(i))

def funcion_2(n):
    if n==0:
        return -1
    if n==1:
        return 2
    else:
        return funcion_2(n-1)*funcion_2(n-2)**3
serie(9)