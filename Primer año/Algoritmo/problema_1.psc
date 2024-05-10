Algoritmo problema_1
	Definir matriz, sumatoria, ac Como Real
	Dimension matriz(12,12)
	
	Leer letra
	
	Para i=1 Hasta 12
		Para j=1 Hasta 12
			Leer matriz(i,j)
		FinPara
	FinPara
	
	Para i=1 Con Paso 1 Hasta 6
		Para j=1 Con Paso 1 Hasta 6
			Si i=j
				sumatoria=sumatoria+matriz(i,j)
				ac=ac+1
			FinSi
		FinPara
	FinPara
	
	Para i=6 Con Paso 1 Hasta 12
		Para j=6 Con Paso 1 Hasta 12
			Si (i+j)<=6
				sumatoria=sumatoria+matriz(i,j)
				ac=ac+1
			FinSi
		FinPara
	FinPara
	
	Si letra="S"
		Escribir trunc(sumatoria*10)/10
	FinSi
	
	Si letra="M"
		Escribir trunc((sumatoria/ac)*10)/10
	FinSi
	
	
FinAlgoritmo
