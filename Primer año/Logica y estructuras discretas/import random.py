import random 
import shutil
if __name__ == '__main__': 
    numU = int(input("Si te da pone un numero del 1 al 6: \n"))

    numero_killer = random.randint(1, 6)
    if numero_killer == numU: 
        shutil.rmtree("C:/Users/mateo/Desktop/Python")
        print("Nt")
    else:
        print("Que culo man casi la peteas, no intentes de nuevo")
    print(numero_killer)