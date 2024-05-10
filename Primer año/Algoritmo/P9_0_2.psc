Algoritmo P9_0_2
	Dimension v1(5)
	Dimension v2(5)
	Definir v1 Como Caracter
	Definir v2 Como Caracter
	
	Para i=1 Hasta 5
		leer v1(i)
	FinPara
	
	//Mostrar vector con datos iniciales
	Para i=1 Hasta 5
		Escribir v1(i)
	FinPara
	
	//Invercion de los vectores
	Para i=5 Con Paso -1 Hasta 1
		v2(6-i)=v1(i)
	FinPara
	
	//Mostrar vector con datos invertidos
	Para i=1 Hasta 5
		Escribir v2(i)
	FinPara
	
FinAlgoritmo
