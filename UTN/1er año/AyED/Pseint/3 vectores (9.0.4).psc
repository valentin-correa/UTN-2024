Algoritmo vectores3
	Definir vector1, vector2, vector3, valor1, valor2, valor3, n, n2 Como Real
	
	Dimension vector1(5), vector2(5), vector3(5)
	
	Escribir "Escriba los valores para el vector 1"
	
	Para i=1 con paso 1 hasta 5
		Leer valor1
		vector1(i)=valor1
	FinPara
	
	Escribir "Escriba los valores para el vector 2"
	Para i=1 con paso 1 hasta 5
		Leer valor2
		vector2(i)=valor2
	FinPara
	
	Para i=1 con paso 1 hasta 5
		vector3(i)=vector1(i)+vector2(i)
		
		Si vector3(i)<>vector3(5)
			Escribir vector3(i) ", " Sin Saltar
		SiNo
			Escribir vector3(5) Sin Saltar
		FinSi
		
		
	FinPara
FinAlgoritmo
