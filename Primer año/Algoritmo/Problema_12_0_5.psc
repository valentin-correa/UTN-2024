Algoritmo Problema_12_0_5
	Dimension matriz(5,5)
	
	Para i=1 Hasta 5
		Para j=1 Hasta 5
			si i=1
				matriz(i,j)=1
			FinSi
			si j=1
				matriz(i,j)=1
			FinSi
			si i=5
				matriz(i,j)=1
			FinSi
			si j=5
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
