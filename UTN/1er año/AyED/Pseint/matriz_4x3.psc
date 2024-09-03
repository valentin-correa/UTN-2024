Algoritmo matriz_4x3
	Dimension matriz(4,3)
	
	para i=1 con paso 1 hasta 4
		para j=1 con paso 1 hasta 3
			Escribir "Escriba los valores de la matriz"
			leer matriz(i,j)
		FinPara
	FinPara
	
	//Suma de filas
	para i=1 con paso 1 hasta 4
		para j=1 con paso 1 hasta 3
			acum=acum+matriz(i,j)
		FinPara
		Escribir "La suma de los elementos de la columna " i " es de: " acum
		acum=0
	FinPara
	Escribir "-----------------------------------------------------"
	
	//Suma de columnas
	para j=1 con paso 1 hasta 3
		para i=1 con paso 1 hasta 4
			acum=acum+matriz(i,j)
		FinPara
		Escribir "La suma de los elementos de la fila " j " es de: " acum
		acum=0
	FinPara
	
	para j=1 con paso 1 hasta 3
		para i=1 con paso 1 hasta 4
			acum=acum+matriz(i,j)
		FinPara
	FinPara
	Escribir "-----------------------------------------------------"
	Escribir "La suma de los elementos de la matriz es de: " acum
	
FinAlgoritmo
