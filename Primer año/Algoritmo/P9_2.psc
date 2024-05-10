Algoritmo P9_2
	Dimension num(5)
	Para i=1 Hasta 5
		leer num(i)
	FinPara
	difmeno=abs(num(1)-num(2))
	Para i=1 Hasta 4
		dif=num(i)-num(i+1)
		
		dif=abs(dif)
		
		
		si difmeno>dif
			difmeno=dif
		FinSi
		
	FinPara  
	Escribir difmeno
FinAlgoritmo