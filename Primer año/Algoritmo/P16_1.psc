SubAlgoritmo return=comprobar(a,b,c)
	si a=b y b=c Entonces
		return=20
	FinSi
	
	si a<>b y b<>c Entonces
		return=0
	FinSi
	
	si a=b y a<>c o a=c y a<>b o b=c y b<>c
		return=10
	FinSi
FinSubAlgoritmo

Algoritmo P16_1
	leer a,b,c
    Escribir comprobar(a,b,c)
FinAlgoritmo
