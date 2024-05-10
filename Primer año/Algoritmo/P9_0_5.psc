Algoritmo P9_0_5
	Dimension vendedores(3)
	Dimension ventas(3)
	Definir vendedores Como Caracter
	Definir ventas, mayo Como Entero
	mayo=0
	meno=0
	
	Para i=1 Hasta 3
		Escribir "Escribir el nombre del vendedor numero ", i
		Leer vendedores(i)
	FinPara
	
	Para i=1 Hasta 3
		Escribir "Escribir las ventas del vendedor numero ", i
		Leer ventas(i)
	FinPara

	Para i=1 Hasta 3
		si ventas(i)>mayo
			mayo=ventas(i)
			negociante=vendedores(i)
		FinSi
	FinPara
	Para i=1 Hasta 3
		si ventas(i)<mayo
			meno=ventas(i)
			mal=vendedores(i)
		FinSi
	FinPara
	
	Escribir "El vendedor que mas vendio fue ", negociante, " con $", mayo, " de ventas"
	Escribir "El vendedor que menos vendio fue ", mal, " con $", meno, " de ventas"
FinAlgoritmo
