Algoritmo Array10
	Definir array, valor1 Como Real
	Dimension array(10)
	
	Escribir "Ingrese 10 valores, si ingresa uno negativo finalizará el arreglo"
	
	Para i=1 con paso 1 hasta 10
		Leer valor1
		Si valor1<0
			i=10
		FinSi
		array(i)=valor1
	FinPara
	
	Para i=1 con paso 1 hasta 10
		Si array(i)=array(10)
			array(10)=0
			Escribir array(10)
		SiNo
			Escribir array(i) ", " Sin Saltar
		FinSi
	FinPara
FinAlgoritmo
