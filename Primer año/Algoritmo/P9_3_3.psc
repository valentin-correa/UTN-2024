Algoritmo P9_3_3
	Escribir "ingrese la cantidad de numeros a calcular"
	Leer n
	Dimension x(n)
	
	//Ingreso de valores/datos
	Escribir "ingrese los valores"
	Para i=1 Hasta n
		leer x(i)
	FinPara
	
	//Calculo de de valores
	Para i=1 Hasta n
		x(i)=1/x(i)
	FinPara
	
	//sumatoria de los valores
	Para i=1 Hasta n
		sumatoriaX=x(i)+sumatoriaX
	FinPara
	
	//Calculo de la division
	Resultado=n/sumatoriaX
	
	//Mostrar Resultado
	Escribir "La raiz del valor cuadratico medio es ", Resultado
FinAlgoritmo
