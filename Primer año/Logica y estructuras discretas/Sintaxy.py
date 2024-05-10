#Como crear un subproceso procedimiento
def nombre_subproceso():
    print("Hola mundo soy un procedimiento siendo ejecutado")
#como crear un subproceso funcion
def nombre_funcion(variable,variable2):
    resultado= variable2 + variable
    return resultado
def Visto():
    #Como se ingresan datos por teclado con leyenda
    a=input("Ingrese su primer numero: ")
    b=input("Ingrese su segundo numero: ")

    #Como se asigna que tipo de dato es
    a=int(a)
    b=int(b)

    #Como hacer ambas cosas al mismo tiempo
    a=int(input("Ingrese su primer numero: "))
    b=int(input("Ingrese su segundo numero: "))

    #llamado de funciones
    nombre_subproceso()
    nombre_funcion(a,b)




    #Cadenas de caracteres
    cad1="Hoy es miercoles"
    #posicion H=0, o=1, y=2, _=3, e=4, s=5, _=6, m=7, i=8, e=9, r=10, c=11, o=12, l=13, e=14, s=15



    #funciones de caracteres
    pasar_a_mayuscula=cad1.upper() #Pasa toda a mayusculas
    pasar_a_minusculas=cad1.lower() #Pasa todo a minusculas
    sustraer=cad1[7:9] 
    #Extrae desde la posicion 7 hasta la posicion 9
    #Osea que sustraer vale ahora "mi"
    tamaño=len(cad1)



    #Operadores logicos
     #Igual logico
     #10==10
     #Distinto logico
     #10!=3

#Como crear vectores
vector=[int() for i in range (3)]

#Como cargar un vector
for i in range (3):
    vector[i] = input()

#Como imprimir un vector completo
print(vector)

#Como imprimir un elemento de un vector
print(vector[0])

#Como crear una matriz
Matriz=[[int() for filas in range (10)]for columnas in range(10)]

#Como cargar una matriz
for filas in range(10):
    for columnas in range(10):
        Matriz[filas][columnas]=int(input())

#Como imprimir una matriz completa
print(Matriz)

#Como imprimir un elemento de la matriz
print(Matriz[0,0])
