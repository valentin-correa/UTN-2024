def Renglon():
    print("..........................")

def Reflexiva(Matrix,Noob):
    lol=1
    Vector=[]
    for i in range(Noob):
        if Matrix[i][i]!=1:
            lol=0
            Matrix[i][i]=1
            Vector.append("["+str(i+1)+";"+str(i+1)+"]")
    if lol==0:
        print("La Matriz no es reflexiva, Quieres su Cerradura?")
        answer=str(input("       "))
        if answer=="si":
            for i in range (Noob):
                print(Matrix[i])
            print("Las relaciones agregadas fueron: ", Vector)
            return (0)
    else:
        print("La Matriz es reflexiva")
        return(1)
        
def Simétrica(Matrix,Noob):
    lol=1
    MT=MatrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]!=Matrix[i][j]:
                lol=0
                Matrix[i][j]=1
                Vector.append("["+str(i+1)+";"+str(j+1)+"]")
    if lol==0:
        Renglon()
        print("La Matriz no es Simétrica, Quieres su Cerradura?")
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
        print("La Matriz es Simétrica")
        Renglon()
        return(1)
def MatrizTranspuesta(Matris,Nuevo):
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
                if Matrix[i][j]==1 and Matriz[j][k]==1:
                    if Matriz[i][k]!=1:
                        lol=0
                        Matrix[i][k]=1
                        Vector.append("["+str(i+1)+";"+str(k+1)+"]")
    trol=trol-1
    if trol==0:
        if lol==0:
            Renglon()
            print("La Matriz no es transitiva, Quieres su Cerradura?")
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
            print("La Matriz es transitiva")
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
        print("La Matriz no es irreflexiva")
    else:
        print("La Matriz es irreflexiva")

def Asimétrica(Matrix, Noob):
    lol=1
    MT=MatrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]==Matrix[i][j]:
                lol=0
    if lol==0:
        Renglon()
        print("La Matriz no es Asimétrica")
        Renglon()
    else:
        Renglon()
        print("La Matriz es Asimétrica")
        Renglon()

def Antisimétrica(Matrix,Noob):
    lol=1
    MT=MatrizTranspuesta(Matrix,Noob)
    Vector=[]
    for i in range(Noob):
        for j in range(Noob):
            if MT[i][j]!=Matrix[i][j] and i!=j:
                lol=0
    if lol==0:
        Renglon()
        print("La Matriz no es Antisimétrica")
        Renglon()
    else:
        Renglon()
        print("La Matriz es Antsiimétrica")
        Renglon()


print(" Ingrese el número  de nodos:")
Nodos=int(input("        "))
Matril=[[None for i in range(Nodos)]for j in range(Nodos)]
Matrip=[[None for i in range(Nodos)]for j in range(Nodos)]
Matrin=[[None for i in range(Nodos)]for j in range(Nodos)]
Matriz=[[None for i in range(Nodos)]for j in range(Nodos)]
Matrik=[[None for i in range(Nodos)]for j in range(Nodos)]
Matriy=[[None for i in range(Nodos)]for j in range(Nodos)]
Matrig=[[None for i in range(Nodos)]for j in range(Nodos)]

for i in range (Nodos):
    for j in range (Nodos):
        print("Ingrese el número de la relación ","[", i+1,";", j+1,"]")
        Matriz[i][j]=int(input("        "))
        Matrin[i][j]=Matriz[i][j]
        Matrip[i][j]=Matriz[i][j]
        Matril[i][j]=Matriz[i][j]
        Matrik[i][j]=Matriz[i][j]
        Matriy[i][j]=Matriz[i][j]
        Matrig[i][j]=Matriz[i][j]
for i in range(Nodos):
    print(Matriz[i])
Renglon()
Reflex=Reflexiva(Matrip,Nodos)
Irreflex=Irreflexiva(Matrik,Nodos)
Sim=Simétrica(Matrin,Nodos)
Asim=Asimétrica(Matriy,Nodos)
Anti=Antisimétrica(Matrig,Nodos)
trol=Nodos
Vector=[]
Trans=Transitiva(Matril,Nodos,trol,Vector)
