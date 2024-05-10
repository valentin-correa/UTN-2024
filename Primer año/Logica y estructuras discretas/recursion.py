def funcion(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n!=1 or n!=2:
        return funcion(n-1)+funcion(n-2)
    


def serie(n):
    for i in range(1,n+1):
        print(funcion(i))

funcion(0)
