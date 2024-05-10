Algoritmo Problema_12_0_3
	Dimension matriz(10,10)
	
	matriz(1,1)=0
	matriz(1,2)=1
	matriz(1,3)=2
	matriz(1,4)=3
	matriz(1,5)=4
	matriz(1,6)=5
	matriz(1,7)=6
	matriz(1,8)=7
	matriz(1,9)=8
	matriz(1,10)=9
	
	matriz(2,1)=1
	matriz(3,1)=2
	matriz(4,1)=3
	matriz(5,1)=4
	matriz(6,1)=5
	matriz(7,1)=6
	matriz(8,1)=7
	matriz(9,1)=8
	matriz(10,1)=9
	
	Para  i=1 Hasta 10
		Para j=1 Hasta 10
			Escribir matriz(i,j)," " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	Para i=2 Hasta 10
		Para j=2 Hasta 10
			matriz(i,j)=matriz(1,j)*matriz(i,1)
		FinPara
	FinPara
	Escribir "Tabla de multiplicar"
	
	
	Para  i=1 Hasta 10
		Para j=1 Hasta 10
			Escribir matriz(i,j)," " Sin Saltar
		FinPara
		Escribir ""
	FinPara
FinAlgoritmo
