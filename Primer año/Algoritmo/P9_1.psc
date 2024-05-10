Algoritmo P9_1
	Dimension num(5)
	Para i=1 Hasta 5
		leer num(i)
	FinPara
	
	Para i=1 Hasta 4
			dif=num(i)-num(i+1)
			dif=abs(dif)
		si difmay<dif
			difmay=dif
		FinSi
	FinPara
	Escribir difmay
FinAlgoritmo
