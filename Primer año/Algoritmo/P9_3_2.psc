Algoritmo P9_3_2
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
		x(i)=x(i)^2
	FinPara
	
	//sumatoria de los valores
	Para i=1 Hasta n
		sumatoriaX=x(i)+sumatoriaX
	FinPara
	
	//Calculo de 1/n
	b=(1/n)
	
	//Calculo de la raiz
	Resultado=Raiz(b*sumatoriaX)
	
	//Mostrar Resultado
	Escribir "La raiz del valor cuadratico medio es ", Resultado
FinAlgoritmo
