Algoritmo DifMax
	Definir VectorA, valores, dif, difmay Como Real
	Definir n Como Entero
	
	Escribir "Escriba la dimensión del vector A"
	Leer n
	Dimension VectorA(n)
	
	Escribir "Ingrese los valores del vector A"
	Para i=1 hasta n con paso 1
		Leer valores
		VectorA(i)=valores
	FinPara
	
	difmay=abs(VectorA(1)-VectorA(2))

	Para i=2 hasta n-1 con paso 1
		dif=VectorA(i)-VectorA(i+1)
		dif=abs(dif)
		si dif>difmay
			difmay=dif
		FinSi
	FinPara
	Escribir "La diferencia máxima es: " difmay
	
FinAlgoritmo
