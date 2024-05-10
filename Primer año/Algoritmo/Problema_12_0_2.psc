Algoritmo Problema_12_0_2
	Dimension matriz(5,3)
	
	//Ingreso
	Para j=1 hasta 2
		Para i=1 Hasta 5
			Leer matriz(i,j)
		FinPara
	FinPara
	
	//suma
	Para i=1 Hasta 5
		matriz(i,3)=matriz(i,1)+matriz(i,2)
	FinPara
FinAlgoritmo
