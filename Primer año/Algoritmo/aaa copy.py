import time

def crear_D(R):
    D=""
    for i in range(R):
        D+=str(i)
        if len(D)>=R:
            return D

#def primerValor(L,R):
    

def determinarMayor(cad):
    mayor=0
    for i in range(len(cad)):
        if int(cad[i:i+k])>mayor:
            mayor=int(cad[i:i+k])
    return mayor

k=int(input())
L, R=map(int, input().split())

start_time = time.time()

D=crear_D(R)

cad=D[L:R+1]

print(determinarMayor(cad))


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")