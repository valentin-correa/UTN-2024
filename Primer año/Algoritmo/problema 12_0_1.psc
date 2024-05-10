Algoritmo Problema_12_0_1
	Dimension matriz(4,3)
	Para i=1 hasta 4
		Para j=1 Hasta 3
			Leer matriz(i,j)
		FinPara
	FinPara
	
	Para i=1 hasta 4
		Para j=1 Hasta 3
			ac=ac+matriz(i,j)
		FinPara
		Escribir "La fila ",i," tiene " , ac
		ac=0
	FinPara
	
	Para j=1 hasta 3
		Para i=1 Hasta 4
			ac=ac+matriz(i,j)
		FinPara
		Escribir "la columna ",j, " tiene ", ac
		ac=0
	FinPara
	
	Para j=1 hasta 3
		Para i=1 Hasta 4
			ac=ac+matriz(i,j)
		FinPara
	FinPara
	Escribir "La suma de todo es ", ac
	
FinAlgoritmo
