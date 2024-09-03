def Reflexiva(Matrix,Noob):
    lol=1
    Vector=[]
    for i in range(Noob):
        if Matrix[i][i]!=1:
            lol=0
            Matrix[i][i]=1
            Vector.append("["+str(i+1)+";"+str(i+1)+"]")
    if lol==0:
        print("La matriz no es reflexiva, Quieres su Cerradura?")
        answer=str(input("       "))
        if answer=="si":
            for i in range (Noob):
                print(Matrix[i])
            print("Las relaciones agregadas fueron: ", Vector)
            return (0)
    else:
        print("La matriz es reflexiva")
        return(1)
        
def Simétrica(Matrix,Noob):
    lol=1
    MT=matrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]!=Matrix[i][j]:
                lol=0
                Matrix[i][j]=1
                Vector.append("["+str(i+1)+";"+str(j+1)+"]")
    if lol==0:
        print("La matriz no es Simétrica, Quieres su Cerradura?")
        answer=str(input("       "))
        if answer=="si":
            for i in range (Noob):
                print(Matrix[i])
            print("Las relaciones agregadas fueron: ", Vector)
            return(0)
    else:
        print("La matriz es Simétrica")
        return(1)
    
def matrizTranspuesta(Matris,Nuevo):
    MT=[[None for i in range(Nuevo)]for j in range(Nuevo)]
    for i in range(Nuevo):
        for j in range(Nuevo):
            MT[i][j]=Matris[j][i]
    return (MT)

def Transitiva(Matrix,Noob,trol,Vector):
    lol=1
    for i in range(Noob):
        for j in range(Noob):
            for k in range(Noob):
                if Matrix[i][j] == 1 and matriz[j][k] == 1:
                    if matriz[i][k]!=1:
                        lol=0
                        Matrix[i][k]=1
                        Vector.append("["+str(i+1)+";"+str(k+1)+"]")
    trol=trol-1
    if trol==0:
        if lol==0:
            Renglon()
            print("La matriz no es transitiva, Quieres su Cerradura?")
            Renglon()
            answer=str(input("       "))
            if answer=="si":
                for i in range (Noob):
                    print(Matrix[i])
                Renglon()
                print("Las relaciones agregadas fueron: ", Vector)
                Renglon()
                return(0)
        else:
            Renglon()
            print("La matriz es transitiva")
            Renglon()
            return(1)
    else:
        Transitiva(Matrix,Noob,trol,Vector)

def Irreflexiva(Matrix,Noob):
    lol=1
    Vector=[]
    for i in range(Noob):
        if Matrix[i][i]==1:
            lol=0     
    if lol==0:
        print("La matriz no es irreflexiva")
    else:
        print("La matriz es irreflexiva")

def Asimétrica(Matrix, Noob):
    lol=1
    MT=matrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]==Matrix[i][j]:
                lol=0
    if lol==0:
        Renglon()
        print("La matriz no es Asimétrica")
        Renglon()
    else:
        Renglon()
        print("La matriz es Asimétrica")
        Renglon()

def Antisimétrica(Matrix,Noob):
    lol=1
    MT=matrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]!=Matrix[i][j] and i!=j:
                lol=0
    if lol==0:
        Renglon()
        print("La matriz no es Antisimétrica")
        Renglon()
    else:
        Renglon()
        print("La matriz es Antsiimétrica")
        Renglon()

Nodos = int(input("Ingrese el número de vértices: "))

matriz = []
for i in range(3):
    matriz.append(input().split())
for i in range(Nodos):
    print(matriz[i])
    
Reflex = Reflexiva(matriz, Nodos)
Irreflex = Irreflexiva(matriz, Nodos)
Sim = Simétrica(matriz, Nodos)
Asim = Asimétrica(matriz, Nodos)
Anti = Antisimétrica(matriz, Nodos)
trol = Nodos
Vector = []
Trans = Transitiva(matriz, Nodos, trol, Vector)
