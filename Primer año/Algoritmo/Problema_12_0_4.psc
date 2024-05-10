Algoritmo Problema_12_0_4
	Dimension matriz(5,5)
	
	Para i=1 Hasta 5
		Para j=1 Hasta 5
			si i=j
				matriz(i,j)=1
			FinSi
		FinPara
	FinPara
	
	
	Para  i=1 Hasta 5
		Para j=1 Hasta 5
			Escribir matriz(i,j)," " Sin Saltar
		FinPara
		Escribir ""
	FinPara
FinAlgoritmo
